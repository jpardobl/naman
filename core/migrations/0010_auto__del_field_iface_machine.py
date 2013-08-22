# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Iface.machine'
        db.delete_column(u'core_iface', 'machine_id')

        # Adding M2M table for field machines on 'Iface'
        m2m_table_name = db.shorten_name(u'core_iface_machines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iface', models.ForeignKey(orm[u'core.iface'], null=False)),
            ('machine', models.ForeignKey(orm[u'core.machine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iface_id', 'machine_id'])


    def backwards(self, orm):
        # Adding field 'Iface.machine'
        db.add_column(u'core_iface', 'machine',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='interfaces', to=orm['core.Machine']),
                      keep_default=False)

        # Removing M2M table for field machines on 'Iface'
        db.delete_table(db.shorten_name(u'core_iface_machines'))


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
            'Meta': {'object_name': 'Iface'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gw': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '39', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'unique': 'True', 'max_length': '39', 'blank': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'interfaces'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['core.Machine']"}),
            'mask': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'nat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Machine'},
            'dns_zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DNSZone']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Environment']"}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15', 'blank': 'True'}),
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
        u'core.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iface': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Iface']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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