# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Iface.mac'
        db.add_column(u'core_iface', 'mac',
                      self.gf('django.db.models.fields.CharField')(max_length=17, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Iface.nat'
        db.add_column(u'core_iface', 'nat',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Iface.mac'
        db.delete_column(u'core_iface', 'mac')

        # Deleting field 'Iface.nat'
        db.delete_column(u'core_iface', 'nat')


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
        u'core.excludediprange': {
            'Meta': {'object_name': 'ExcludedIPRange'},
            'first': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'vlan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'excluded_ranges'", 'to': u"orm['core.VLan']"})
        },
        u'core.hostnamesequence': {
            'Meta': {'object_name': 'HostnameSequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'core.iface': {
            'Meta': {'unique_together': "(('ip',),)", 'object_name': 'Iface'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'interfaces'", 'to': u"orm['core.Machine']"}),
            'mask': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'nat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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