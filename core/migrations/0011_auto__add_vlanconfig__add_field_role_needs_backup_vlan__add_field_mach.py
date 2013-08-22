# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VLanConfig'
        db.create_table(u'core_vlanconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Machine'])),
        ))
        db.send_create_signal(u'core', ['VLanConfig'])

        # Adding M2M table for field vlans on 'VLanConfig'
        m2m_table_name = db.shorten_name(u'core_vlanconfig_vlans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vlanconfig', models.ForeignKey(orm[u'core.vlanconfig'], null=False)),
            ('vlan', models.ForeignKey(orm[u'core.vlan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vlanconfig_id', 'vlan_id'])

        # Adding field 'Role.needs_backup_vlan'
        db.add_column(u'core_role', 'needs_backup_vlan',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Machine.dmz_located'
        db.add_column(u'core_machine', 'dmz_located',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'VLan.management_purpose'
        db.add_column(u'core_vlan', 'management_purpose',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'VLan.general_pupose_service'
        db.add_column(u'core_vlan', 'general_pupose_service',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding M2M table for field backup_vlans on 'Environment'
        m2m_table_name = db.shorten_name(u'core_environment_backup_vlans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('environment', models.ForeignKey(orm[u'core.environment'], null=False)),
            ('vlan', models.ForeignKey(orm[u'core.vlan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['environment_id', 'vlan_id'])

        # Adding M2M table for field service_vlans on 'Environment'
        m2m_table_name = db.shorten_name(u'core_environment_service_vlans')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('environment', models.ForeignKey(orm[u'core.environment'], null=False)),
            ('vlan', models.ForeignKey(orm[u'core.vlan'], null=False))
        ))
        db.create_unique(m2m_table_name, ['environment_id', 'vlan_id'])

        # Adding field 'Project.dmz'
        db.add_column(u'core_project', 'dmz',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.VLan'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'VLanConfig'
        db.delete_table(u'core_vlanconfig')

        # Removing M2M table for field vlans on 'VLanConfig'
        db.delete_table(db.shorten_name(u'core_vlanconfig_vlans'))

        # Deleting field 'Role.needs_backup_vlan'
        db.delete_column(u'core_role', 'needs_backup_vlan')

        # Deleting field 'Machine.dmz_located'
        db.delete_column(u'core_machine', 'dmz_located')

        # Deleting field 'VLan.management_purpose'
        db.delete_column(u'core_vlan', 'management_purpose')

        # Deleting field 'VLan.general_pupose_service'
        db.delete_column(u'core_vlan', 'general_pupose_service')

        # Removing M2M table for field backup_vlans on 'Environment'
        db.delete_table(db.shorten_name(u'core_environment_backup_vlans'))

        # Removing M2M table for field service_vlans on 'Environment'
        db.delete_table(db.shorten_name(u'core_environment_service_vlans'))

        # Deleting field 'Project.dmz'
        db.delete_column(u'core_project', 'dmz_id')


    models = {
        u'core.dnszone': {
            'Meta': {'object_name': 'DNSZone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.environment': {
            'Meta': {'object_name': 'Environment'},
            'backup_vlans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'backedup_environments'", 'symmetrical': 'False', 'to': u"orm['core.VLan']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_vlans': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'served_environments'", 'symmetrical': 'False', 'to': u"orm['core.VLan']"})
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
            'dmz_located': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'dmz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.VLan']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.role': {
            'Meta': {'object_name': 'Role'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_backup_vlan': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
            'general_pupose_service': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Machine']"}),
            'vlans': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.VLan']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['core']