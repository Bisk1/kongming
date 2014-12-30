# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'WordPLExercise'
        db.delete_table(u'chinesetool_wordplexercise')

        # Deleting model 'SentenceZHExercise'
        db.delete_table(u'chinesetool_sentencezhexercise')

        # Deleting model 'WordZHExercise'
        db.delete_table(u'chinesetool_wordzhexercise')

        # Deleting model 'ExplanationExercise'
        db.delete_table(u'chinesetool_explanationexercise')

        # Deleting model 'SentencePLExercise'
        db.delete_table(u'chinesetool_sentenceplexercise')

        # Adding model 'SentenceZHExerciseDetails'
        db.create_table(u'chinesetool_sentencezhexercisedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('sentence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.SentenceZH'])),
        ))
        db.send_create_signal(u'chinesetool', ['SentenceZHExerciseDetails'])

        # Adding model 'SentencePLExerciseDetails'
        db.create_table(u'chinesetool_sentenceplexercisedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('sentence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.SentencePL'])),
        ))
        db.send_create_signal(u'chinesetool', ['SentencePLExerciseDetails'])

        # Adding model 'ExplanationExerciseDetails'
        db.create_table(u'chinesetool_explanationexercisedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'chinesetool', ['ExplanationExerciseDetails'])

        # Adding model 'WordZHExerciseDetails'
        db.create_table(u'chinesetool_wordzhexercisedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordZHExerciseDetails'])

        # Adding model 'WordPLExerciseDetails'
        db.create_table(u'chinesetool_wordplexercisedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordPLExerciseDetails'])


    def backwards(self, orm):
        # Adding model 'WordPLExercise'
        db.create_table(u'chinesetool_wordplexercise', (
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordPL'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordPLExercise'])

        # Adding model 'SentenceZHExercise'
        db.create_table(u'chinesetool_sentencezhexercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('sentence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.SentenceZH'])),
        ))
        db.send_create_signal(u'chinesetool', ['SentenceZHExercise'])

        # Adding model 'WordZHExercise'
        db.create_table(u'chinesetool_wordzhexercise', (
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.WordZH'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
        ))
        db.send_create_signal(u'chinesetool', ['WordZHExercise'])

        # Adding model 'ExplanationExercise'
        db.create_table(u'chinesetool_explanationexercise', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
        ))
        db.send_create_signal(u'chinesetool', ['ExplanationExercise'])

        # Adding model 'SentencePLExercise'
        db.create_table(u'chinesetool_sentenceplexercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise'])),
            ('sentence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.SentencePL'])),
        ))
        db.send_create_signal(u'chinesetool', ['SentencePLExercise'])

        # Deleting model 'SentenceZHExerciseDetails'
        db.delete_table(u'chinesetool_sentencezhexercisedetails')

        # Deleting model 'SentencePLExerciseDetails'
        db.delete_table(u'chinesetool_sentenceplexercisedetails')

        # Deleting model 'ExplanationExerciseDetails'
        db.delete_table(u'chinesetool_explanationexercisedetails')

        # Deleting model 'WordZHExerciseDetails'
        db.delete_table(u'chinesetool_wordzhexercisedetails')

        # Deleting model 'WordPLExerciseDetails'
        db.delete_table(u'chinesetool_wordplexercisedetails')


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
        u'chinesetool.exercise': {
            'Meta': {'object_name': 'Exercise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Lesson']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseType']"})
        },
        u'chinesetool.exerciseaction': {
            'Meta': {'object_name': 'ExerciseAction'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.LessonAction']"}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'NO-DESC'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'NO-NAME'", 'max_length': '20'})
        },
        u'chinesetool.explanationexercisedetails': {
            'Meta': {'object_name': 'ExplanationExerciseDetails'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'chinesetool.lesson': {
            'Meta': {'object_name': 'Lesson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chinesetool.Lesson']", 'symmetrical': 'False'}),
            'topic': ('django.db.models.fields.CharField', [], {'default': "'NO-NAME'", 'max_length': '100'})
        },
        u'chinesetool.lessonaction': {
            'Meta': {'object_name': 'LessonAction'},
            'current_exercise_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fails': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Lesson']", 'null': 'True'}),
            'total_exercises_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'chinesetool.sentencepl': {
            'Meta': {'object_name': 'SentencePL'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'chinesetool.sentenceplexercisedetails': {
            'Meta': {'object_name': 'SentencePLExerciseDetails'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.SentencePL']"})
        },
        u'chinesetool.sentencetranslation': {
            'Meta': {'unique_together': "(['sentence_zh', 'sentence_pl'],)", 'object_name': 'SentenceTranslation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence_pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.SentencePL']"}),
            'sentence_zh': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.SentenceZH']"})
        },
        u'chinesetool.sentencezh': {
            'Meta': {'object_name': 'SentenceZH'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'sentencepl_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chinesetool.SentencePL']", 'through': u"orm['chinesetool.SentenceTranslation']", 'symmetrical': 'False'})
        },
        u'chinesetool.sentencezhexercisedetails': {
            'Meta': {'object_name': 'SentenceZHExerciseDetails'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.SentenceZH']"})
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
        u'chinesetool.wordplexercisedetails': {
            'Meta': {'object_name': 'WordPLExerciseDetails'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.WordPL']"})
        },
        u'chinesetool.wordskill': {
            'Meta': {'object_name': 'WordSkill'},
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
            'pinyin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wordpl_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chinesetool.WordPL']", 'through': u"orm['chinesetool.WordTranslation']", 'symmetrical': 'False'})
        },
        u'chinesetool.wordzhexercisedetails': {
            'Meta': {'object_name': 'WordZHExerciseDetails'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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