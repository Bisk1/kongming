# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'WordZHExerciseAction'
        db.delete_table(u'chinesetool_wordzhexerciseaction')

        # Deleting model 'WordPLExerciseAction'
        db.delete_table(u'chinesetool_wordplexerciseaction')

        # Adding model 'AbstractExerciseActionDescription'
        db.create_table(u'chinesetool_abstractexerciseactiondescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.ExerciseAction'])),
        ))
        db.send_create_signal(u'chinesetool', ['AbstractExerciseActionDescription'])

        # Adding model 'WordPLExerciseActionDescription'
        db.create_table(u'chinesetool_wordplexerciseactiondescription', (
            (u'abstractexerciseactiondescription_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['chinesetool.AbstractExerciseActionDescription'], unique=True, primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordPLExerciseActionDescription'])

        # Adding model 'WordZHExerciseActionDescription'
        db.create_table(u'chinesetool_wordzhexerciseactiondescription', (
            (u'abstractexerciseactiondescription_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['chinesetool.AbstractExerciseActionDescription'], unique=True, primary_key=True)),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordZHExerciseActionDescription'])

        # Adding field 'ExerciseAction.type'
        db.add_column(u'chinesetool_exerciseaction', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.ExerciseType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExerciseAction.number'
        db.add_column(u'chinesetool_exerciseaction', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'ExerciseAction.result'
        db.add_column(u'chinesetool_exerciseaction', 'result',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'WordZHExerciseAction'
        db.create_table(u'chinesetool_wordzhexerciseaction', (
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.ExerciseAction'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordZHExerciseAction'])

        # Adding model 'WordPLExerciseAction'
        db.create_table(u'chinesetool_wordplexerciseaction', (
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
            ('exercise_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.ExerciseAction'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'chinesetool', ['WordPLExerciseAction'])

        # Deleting model 'AbstractExerciseActionDescription'
        db.delete_table(u'chinesetool_abstractexerciseactiondescription')

        # Deleting model 'WordPLExerciseActionDescription'
        db.delete_table(u'chinesetool_wordplexerciseactiondescription')

        # Deleting model 'WordZHExerciseActionDescription'
        db.delete_table(u'chinesetool_wordzhexerciseactiondescription')

        # Deleting field 'ExerciseAction.type'
        db.delete_column(u'chinesetool_exerciseaction', 'type_id')

        # Deleting field 'ExerciseAction.number'
        db.delete_column(u'chinesetool_exerciseaction', 'number')

        # Deleting field 'ExerciseAction.result'
        db.delete_column(u'chinesetool_exerciseaction', 'result')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'chinesetool.abstractexerciseactiondescription': {
            'Meta': {'object_name': 'AbstractExerciseActionDescription'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseAction']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'chinesetool.exerciseaction': {
            'Meta': {'object_name': 'ExerciseAction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.LessonAction']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseType']", 'null': 'True', 'blank': 'True'})
        },
        u'chinesetool.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'chinesetool.lesson': {
            'Meta': {'object_name': 'Lesson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.lessonaction': {
            'Meta': {'object_name': 'LessonAction'},
            'current_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fails': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Lesson']", 'null': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'chinesetool.sentencepl': {
            'Meta': {'object_name': 'SentencePL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sentence': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'chinesetool.sentencetranslation': {
            'Meta': {'object_name': 'SentenceTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence_pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"}),
            'sentence_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"})
        },
        u'chinesetool.sentencezh': {
            'Meta': {'object_name': 'SentenceZH'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sentence': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'chinesetool.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'abo_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'registration_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'chinesetool.wordpl': {
            'Meta': {'object_name': 'WordPL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'chinesetool.wordplexerciseactiondescription': {
            'Meta': {'object_name': 'WordPLExerciseActionDescription', '_ormbases': [u'chinesetool.AbstractExerciseActionDescription']},
            u'abstractexerciseactiondescription_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['chinesetool.AbstractExerciseActionDescription']", 'unique': 'True', 'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"})
        },
        u'chinesetool.wordskills': {
            'Meta': {'object_name': 'WordSkills'},
            'correct': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'correct_run': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'word_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"}),
            'wrong': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.wordtranslation': {
            'Meta': {'unique_together': "(['word_zh', 'word_pl'],)", 'object_name': 'WordTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word_pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"}),
            'word_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"})
        },
        u'chinesetool.wordzh': {
            'Meta': {'unique_together': "(['word', 'pinyin'],)", 'object_name': 'WordZH'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['chinesetool.Lesson']", 'null': 'True'}),
            'pinyin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'wordpl_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chinesetool.WordPL']", 'through': u"orm['chinesetool.WordTranslation']", 'symmetrical': 'False'})
        },
        u'chinesetool.wordzhexerciseactiondescription': {
            'Meta': {'object_name': 'WordZHExerciseActionDescription', '_ormbases': [u'chinesetool.AbstractExerciseActionDescription']},
            u'abstractexerciseactiondescription_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['chinesetool.AbstractExerciseActionDescription']", 'unique': 'True', 'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordZH']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chinesetool']