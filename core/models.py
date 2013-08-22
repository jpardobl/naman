from django.db import models
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
import ipaddr
import logging
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Get an instance of a logger
logger = logging.getLogger(__name__)


class MoreThanOneIfacePerVlanError(Exception):
    pass


class IfaceSequence(models.Model):
    machine = models.ForeignKey("Machine")
    vlan = models.ForeignKey("VLan")
    last_number = models.IntegerField(default=0)

    @property
    def incr(self, ):
        self.last_number += 1
        self.save()
        return self.last_number


class HostnameSequence(models.Model):
    prefix = models.CharField(max_length=11)
    last_number = models.IntegerField(default=0)

    @property
    def next(self, ):
        return self.last_number + 1

    @property
    def incr(self, ):
        self.last_number += 1
        self.save()
        return self.last_number

    def __unicode__(self, ):
        return u"%s(%s)" % (self.prefix, self.last_number)


class CICaracteristic(models.Model):
    code = models.CharField(max_length=4)
    description = models.TextField()

    def __unicode__(self, ):
        return u"%s" % self.code

    class Meta:
        abstract = True


class DNSZone(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self, ):
        return u"%s" % self.name

    def save(self, *args, **kwargs):
        new = False
        if self.pk is None:
            new = True
        super(DNSZone, self).save(*args, **kwargs)
        if new:
            logger.info("New DNSZone created: %s" % self)


class MType(models.Model):
    name = models.CharField(max_length=20)
    auto_name = models.BooleanField(default=True)
    has_serial = models.BooleanField(default=True)

    def __unicode__(self, ):
        return u"%s" % self.name


class Environment(models.Model):
    code = models.CharField(max_length=4, blank=True)
    description = models.TextField()
    backup_vlans = models.ManyToManyField('VLan')
    service_vlans = models.ManyToManyField('VLan', related_name='environments')

    def __unicode__(self, ):
        return u"%s" % self.description


class Role(CICaracteristic):
    needs_backup_vlan = models.BooleanField(default=False)


class OperatingSystem(CICaracteristic):
    pass


class ExcludedIPRange(models.Model):
    first = models.IPAddressField()
    last = models.IPAddressField()
    vlan = models.ForeignKey("VLan", related_name="excluded_ranges")

    class ExcludedIPError(Exception):
        pass

    def __unicode__(self, ):
        return "vlan: %s (%s - %s)" % (self.vlan, self.first, self.last)

    @property
    def as_tuple(self, ):
        return (self.first, self.last)

    def in_range(self, ip):
        if not isinstance(ip, ipaddr.IPv4Address):
            ip = ipaddr.IPv4Address(ip)

        if not isinstance(self.first, ipaddr.IPv4Address):
            self.first = ipaddr.IPv4Address(self.first)

        if not isinstance(self.last, ipaddr.IPv4Address):
            self.last = ipaddr.IPv4Address(self.last)

        if ip in self.as_tuple:
            return True

        if ip > self.first and ip < self.last:
            return True
        return False

    def save(self, *args, **kwargs):

        if not self.vlan.is_ip_valid(self.first):
            raise ipaddr.AddressValueError("First IP is not correct for vlan")
        if not self.vlan.is_ip_valid(self.last):
            raise ipaddr.AddressValueError("Last IP is not correct for vlan")

        super(ExcludedIPRange, self).save(*args, **kwargs)


class VLanManager(models.Manager):

    def get_from_ip(self, ip):

        for vlan in self.all():
            if vlan.is_ip_valid(ip):
                return vlan
        return None


class VLan(models.Model):
    name = models.CharField(max_length=6)
    tag = models.IntegerField()
    ip = models.IPAddressField()
    gw = models.IPAddressField()
    mask = models.IntegerField()
    management_purpose = models.BooleanField(default=False)
    #general_purpose_service = models.BooleanField(default=False)

    class NoFreeIPError(Exception):
        pass

    def __unicode__(self, ):
        return u"%s(%s)" % (self.name, self.tag)

    @property
    def info(self, ):
        hosts = [x for x in self.network.iterhosts()]
        return u"%s; first_ip: %s; last_ip: %s; num_hosts: %s" % (
            self,
            hosts[0],
            hosts[-1],
            len(hosts),
        )

    def is_ip_valid(self, ip):
        """ Calculates if an IP belongs to the vlan addressing scope"""
        if not isinstance(ip, ipaddr.IPv4Address):
            ip = ipaddr.IPv4Address(ip)
        for nip in self.network.iterhosts():
            if nip == ip:
                return True
        return False

    @property
    def network(self, ):
        return ipaddr.IPv4Network("%s/%s" % (self.ip, self.mask))

    @property
    def has_free_ip(self, ):
        return True if self.get_ip() else False

    def get_ip(self, ):
        """ searchs and returns a free IP, respects excluded ranges"""
        eranges = self.excluded_ranges
        print "looking for an IP in scope: %s" % self.network
        for ip in self.network.iterhosts():
            print "trying with IP %s" % ip
            try:
                for erange in eranges.all():
                    if erange.in_range(ip):
                        raise ExcludedIPRange.ExcludedIPError
            except ExcludedIPRange.ExcludedIPError:
                print "IP %s excluded" % ip
                continue

            try:
                Iface.objects.get(ip=str(ip))
            except ObjectDoesNotExist:
                return str(ip)

        return None

    def save(self, *args, **kwargs):
        new = False
        if self.pk is None:
            new = True
        super(VLan, self).save(*args, **kwargs)
        if new:
            logger.info("New VLAN created: %s" % self)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    dmz = models.ForeignKey('VLan', null=True, blank=True)
    service_vlans = models.ManyToManyField('VLan', related_name='projects')
    #machines = models.ManyToManyField("Machine")

    def __unicode__(self, ):
        return u"%s(%s)" % (self.name, self.code)

    def save(self, *args, **kwargs):
        new = False
        if self.pk is None:
            new = True
        super(Project, self).save(*args, **kwargs)
        if new:
            logger.info("New Project created: %s" % self)


class Machine(models.Model):
    hostname = models.CharField(max_length=15, blank=True, unique=True)
    dns_zone = models.ForeignKey(DNSZone)
    environment = models.ForeignKey(Environment)
    role = models.ForeignKey(Role)
    operating_system = models.ForeignKey(OperatingSystem)
    virtual = models.BooleanField(default=True)
    project = models.ForeignKey(
        Project,
        related_name="machines",
        null=True,
        blank=True)
    mtype = models.ForeignKey(MType)
    location = models.CharField(max_length=50, null=True, blank=True)
    dmz_located = models.BooleanField(default=False)
    #close_to = models.ForeignKey(Machine)

    def initialize_hostname(self, ):
        hn = u"%s%s%s%s" % (
            self.role.code,
            self.project.code if self.project is not None else "",
            self.operating_system.code,
            self.environment.code if self.environment.code != "PRO" else "",
            )
        hn = hn.lower()
        if self.mtype.has_serial:
            hn = "%s%s" % (
                hn,
                HostnameSequence.objects.get_or_create(prefix=hn)[0].incr)
        self.hostname = hn

    def save(self, *args, **kwargs):
        new = False

        with transaction.commit_on_success():
            if self.pk is None:
                new = True
                if self.mtype.auto_name and self.hostname in (None, ""):
                    self.initialize_hostname()
                elif self.hostname is None or self.hostname == "":
                    raise AttributeError(
                        "Hostname missing for a non automatic one")

            super(Machine, self).save(*args, **kwargs)
            if new:
                logger.info("New machine created: %s" % self)

    @property
    def fqdn(self, ):
        return u"%s%s" % (self.hostname, self.dns_zone)

    def __unicode__(self, ):
        return u"%s" % self.fqdn

    def has_iface_on_vlan(self, vlan):
        return self.interfaces.filter(vlan=vlan).exists()


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    iface = models.ForeignKey("Iface")


class Iface(models.Model):

    PREFIX = "eth"

    name = models.CharField(max_length=11, blank=True)
    vlan = models.ForeignKey(VLan)
    ip = models.GenericIPAddressField(blank=True, unique=True)
    gw = models.GenericIPAddressField(blank=True, default="0.0.0.0")
    mask = models.IntegerField(blank=True)
    machines = models.ManyToManyField(
        Machine,
        related_name="interfaces",
        null=True,
        blank=True)
    comments = models.TextField(null=True, blank=True)
    mac = models.CharField(max_length=17, null=True, blank=True)
    nat = models.IntegerField(null=True, blank=True)
    virtual = models.BooleanField(default=False)

    def __unicode__(self, ):
        out = "machines: ["
        for m in self.machines.all():
            out = "%s %s, " % (out, m)

        return u"%s]; vlan: %s; ip: %s" % (
            out,
            self.vlan,
            self.ip)

    def save(self, *args, **kwargs):
        new = False
        with transaction.commit_on_success():
            if self.pk is None:
                new = True

                self.ip = self.vlan.get_ip()
                self.gw = self.vlan.gw

            self.mask = self.vlan.mask

            super(Iface, self).save(*args, **kwargs)
            if new:
                logger.info("New Iface created: %s" % self)


class VLanConfig(models.Model):

    machine = models.ForeignKey(Machine)
    vlans = models.ManyToManyField(VLan)
    needs_backup = models.BooleanField(default=True)
    needs_management = models.BooleanField(default=False)

    def __unicode__(self, ):
        out = u"VLan config for %s: [" % self.machine

        for vlan in self.vlans.all().order_by('name'):
            out = "%s %s," % (out, vlan)

        return u"%s]" % out

    def append_vlan(self, vlan):
        """ Adds a new vlan checking if it has free IPs """
        if not vlan.has_free_ip:
            raise VLan.NoFreeIPError(vlan)
        self.vlans.add(vlan)

    def add_backup_vlan(self, ):

        if not self.machine.role.needs_backup_vlan:
            return

        for vlan in self.machine.environment.backup_vlans.all().order_by('name'):
            try:
                self.append_vlan(vlan)
                return
            except VLan.NoFreeIPError:
                continue
        raise VLan.NoFreeIPError("No free IPs at any backup vlan")

    def add_management_vlan(self, ):
        man_vlans = VLan.objects.filter(management_purpose=True)
        if man_vlans.count() == 0:
            raise ImproperlyConfigured("Missing management vlans")

        for vlan in man_vlans:
            try:
                self.append_vlan(vlan)
                return
            except VLan.NoFreeIPError:
                continue

        raise VLan.NoFreeIPError("No free IPs at any management vlan")

    def add_service_vlan(self, ):

        project = self.machine.project

        #adding DMZ
        if self.machine.dmz_located:

            if project is None or project.dmz is None:
                raise ImproperlyConfigured(
                    "DMZ located machine must belong to a project which has dmz vlan assing")
            self.append_vlan(project.dmz)
            return

        # adding campus service vlans for project machine when project
        # has dedicated vlans and environment is production
        if project is not None and self.machine.environment.code == settings.ENV_PROD:
            for vlan in project.service_vlans.all().order_by('name'):
                try:
                    self.append_vlan(vlan)
                    return
                except VLan.NoFreeIPError:
                    continue

        # adding campus service vlans for: (or)
        # - project machines which project hasn't dedicated vlan
        # - no general purpose machines
        # - no production environment

        for vlan in self.machine.environment.service_vlans.all().order_by('name'):
            try:
                self.append_vlan(vlan)
                return
            except VLan.NoFreeIPError:
                continue

        raise VLan.NoFreeIPError("Can't assign free IP for service vlan")

    def save(self, *args, **kwargs):

        new = (self.pk is None)

        super(VLanConfig, self).save(*args, **kwargs)
        if not new:
            return

        #deleting possible previous vlans
        [x.delete for x in self.vlans.all()]
        if self.needs_backup:
            self.add_backup_vlan()
        if self.needs_management:
            self.add_management_vlan()
        self.add_service_vlan()
