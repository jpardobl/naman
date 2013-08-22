# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IfaceSequence'
        db.create_table(u'core_ifacesequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Machine'])),
            ('vlan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.VLan'])),
            ('last_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['IfaceSequence'])

        # Adding model 'HostnameSequence'
        db.create_table(u'core_hostnamesequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('last_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['HostnameSequence'])

        # Adding model 'DNSZone'
        db.create_table(u'core_dnszone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['DNSZone'])

        # Adding model 'MType'
        db.create_table(u'core_mtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('auto_name', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('has_serial', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'core', ['MType'])

        # Adding model 'Environment'
        db.create_table(u'core_environment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Environment'])

        # Adding model 'Role'
        db.create_table(u'core_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Role'])

        # Adding model 'OperatingSystem'
        db.create_table(u'core_operatingsystem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['OperatingSystem'])

        # Adding model 'VLan'
        db.create_table(u'core_vlan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('tag', self.gf('django.db.models.fields.IntegerField')()),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('gw', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('mask', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['VLan'])

        # Adding model 'Project'
        db.create_table(u'core_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'core', ['Project'])

        # Adding model 'Machine'
        db.create_table(u'core_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('dns_zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.DNSZone'])),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Environment'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Role'])),
            ('operating_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.OperatingSystem'])),
            ('virtual', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='machines', null=True, to=orm['core.Project'])),
            ('mtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.MType'])),
        ))
        db.send_create_signal(u'core', ['Machine'])

        # Adding model 'Iface'
        db.create_table(u'core_iface', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('vlan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.VLan'])),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, blank=True)),
            ('gw', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, blank=True)),
            ('mask', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(related_name='interfaces', to=orm['core.Machine'])),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Iface'])


    def backwards(self, orm):
        # Deleting model 'IfaceSequence'
        db.delete_table(u'core_ifacesequence')

        # Deleting model 'HostnameSequence'
        db.delete_table(u'core_hostnamesequence')

        # Deleting model 'DNSZone'
        db.delete_table(u'core_dnszone')

        # Deleting model 'MType'
        db.delete_table(u'core_mtype')

        # Deleting model 'Environment'
        db.delete_table(u'core_environment')

        # Deleting model 'Role'
        db.delete_table(u'core_role')

        # Deleting model 'OperatingSystem'
        db.delete_table(u'core_operatingsystem')

        # Deleting model 'VLan'
        db.delete_table(u'core_vlan')

        # Deleting model 'Project'
        db.delete_table(u'core_project')

        # Deleting model 'Machine'
        db.delete_table(u'core_machine')

        # Deleting model 'Iface'
        db.delete_table(u'core_iface')


    models = {
        u'core.dnszone': {
            'Meta': {'object_name': 'DNSZone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.environment': {
            'Meta': {'object_name': 'Environment'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.hostnamesequence': {
            'Meta': {'object_name': 'HostnameSequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'core.iface': {
            'Meta': {'object_name': 'Iface'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interfaces'", 'to': u"orm['core.Machine']"}),
            'mask': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'vlan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.VLan']"})
        },
        u'core.ifacesequence': {
            'Meta': {'object_name': 'IfaceSequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Machine']"}),
            'vlan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.VLan']"})
        },
        u'core.machine': {
            'Meta': {'object_name': 'Machine'},
            'dns_zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DNSZone']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Environment']"}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.MType']"}),
            'operating_system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.OperatingSystem']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'machines'", 'null': 'True', 'to': u"orm['core.Project']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Role']"}),
            'virtual': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'core.mtype': {
            'Meta': {'object_name': 'MType'},
            'auto_name': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_serial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.project': {
            'Meta': {'object_name': 'Project'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.role': {
            'Meta': {'object_name': 'Role'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.vlan': {
            'Meta': {'object_name': 'VLan'},
            'gw': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'mask': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'tag': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']