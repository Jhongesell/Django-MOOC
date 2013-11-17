# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instructor'
        db.create_table(u'student_portal_instructor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'student_portal', ['Instructor'])

        # Adding model 'Course'
        db.create_table(u'student_portal_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('instructor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Instructor'])),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'student_portal', ['Course'])

        # Adding model 'Lecture'
        db.create_table(u'student_portal_lecture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Course'])),
        ))
        db.send_create_signal(u'student_portal', ['Lecture'])

        # Adding model 'Student'
        db.create_table(u'student_portal_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'student_portal', ['Student'])

        # Adding M2M table for field course on 'Student'
        m2m_table_name = db.shorten_name(u'student_portal_student_course')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'student_portal.student'], null=False)),
            ('course', models.ForeignKey(orm[u'student_portal.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'course_id'])

        # Adding model 'Assignment'
        db.create_table(u'student_portal_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Course'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('points_possible', self.gf('django.db.models.fields.IntegerField')(default=100)),
        ))
        db.send_create_signal(u'student_portal', ['Assignment'])

        # Adding model 'Submission'
        db.create_table(u'student_portal_submission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Course'])),
            ('grade', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Assignment'])),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_portal.Student'])),
            ('docfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'student_portal', ['Submission'])


    def backwards(self, orm):
        # Deleting model 'Instructor'
        db.delete_table(u'student_portal_instructor')

        # Deleting model 'Course'
        db.delete_table(u'student_portal_course')

        # Deleting model 'Lecture'
        db.delete_table(u'student_portal_lecture')

        # Deleting model 'Student'
        db.delete_table(u'student_portal_student')

        # Removing M2M table for field course on 'Student'
        db.delete_table(db.shorten_name(u'student_portal_student_course'))

        # Deleting model 'Assignment'
        db.delete_table(u'student_portal_assignment')

        # Deleting model 'Submission'
        db.delete_table(u'student_portal_submission')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'student_portal.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Course']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'points_possible': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'student_portal.course': {
            'Meta': {'object_name': 'Course'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Instructor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'student_portal.instructor': {
            'Meta': {'object_name': 'Instructor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'student_portal.lecture': {
            'Meta': {'object_name': 'Lecture'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        },
        u'student_portal.student': {
            'Meta': {'object_name': 'Student'},
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['student_portal.Course']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'student_portal.submission': {
            'Meta': {'object_name': 'Submission'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Assignment']"}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Course']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'grade': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['student_portal.Student']"})
        }
    }

    complete_apps = ['student_portal']