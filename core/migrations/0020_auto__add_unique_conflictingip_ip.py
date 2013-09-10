# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ConflictingIP', fields ['ip']
        db.create_unique(u'core_conflictingip', ['ip'])


    def backwards(self, orm):
        # Removing unique constraint on 'ConflictingIP', fields ['ip']
        db.delete_unique(u'core_conflictingip', ['ip'])


    models = {
        u'core.conflictingip': {
            'Meta': {'object_name': 'ConflictingIP'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39'})
        },
        u'core.dnszone': {
            'Meta': {'object_name': 'DNSZone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.environment': {
            'Meta': {'object_name': 'Environment'},
            'backup_vlans': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.VLan']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_vlans': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'environments'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.VLan']"})
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
            'Meta': {'object_name': 'Iface'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '39', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'interfaces'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.Machine']"}),
            'mask': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'nat': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'virtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'Meta': {'ordering': "('hostname',)", 'object_name': 'Machine'},
            'dmz_located': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dns_zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DNSZone']", 'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Environment']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.MType']", 'null': 'True', 'blank': 'True'}),
            'operating_system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.OperatingSystem']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'machines'", 'null': 'True', 'to': u"orm['core.Project']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Role']", 'null': 'True', 'blank': 'True'}),
            'virtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'dmz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.VLan']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'service_vlans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['core.VLan']"})
        },
        u'core.role': {
            'Meta': {'object_name': 'Role'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_backup_vlan': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iface': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Iface']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.vlan': {
            'Meta': {'ordering': "('name',)", 'object_name': 'VLan'},
            'gw': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'management_purpose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mask': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'tag': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.vlanconfig': {
            'Meta': {'object_name': 'VLanConfig'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vlan_configs'", 'to': u"orm['core.Machine']"}),
            'needs_backup': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'needs_management': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vlans': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.VLan']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']