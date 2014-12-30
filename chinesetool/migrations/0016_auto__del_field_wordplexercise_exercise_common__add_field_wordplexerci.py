# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'WordPLExercise.exercise_common'
        db.delete_column(u'chinesetool_wordplexercise', 'exercise_common_id')

        # Adding field 'WordPLExercise.exercise'
        db.add_column(u'chinesetool_wordplexercise', 'exercise',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'SentenceZHExercise.exercise_common'
        db.delete_column(u'chinesetool_sentencezhexercise', 'exercise_common_id')

        # Adding field 'SentenceZHExercise.exercise'
        db.add_column(u'chinesetool_sentencezhexercise', 'exercise',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'WordZHExercise.exercise_common'
        db.delete_column(u'chinesetool_wordzhexercise', 'exercise_common_id')

        # Adding field 'WordZHExercise.exercise'
        db.add_column(u'chinesetool_wordzhexercise', 'exercise',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'ExplanationExercise.exercise_common'
        db.delete_column(u'chinesetool_explanationexercise', 'exercise_common_id')

        # Adding field 'ExplanationExercise.exercise'
        db.add_column(u'chinesetool_explanationexercise', 'exercise',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'SentencePLExercise.exercise_common'
        db.delete_column(u'chinesetool_sentenceplexercise', 'exercise_common_id')

        # Adding field 'SentencePLExercise.exercise'
        db.add_column(u'chinesetool_sentenceplexercise', 'exercise',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chinesetool.Exercise']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'WordPLExercise.exercise_common'
        raise RuntimeError("Cannot reverse this migration. 'WordPLExercise.exercise_common' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'WordPLExercise.exercise_common'
        db.add_column(u'chinesetool_wordplexercise', 'exercise_common',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'WordPLExercise.exercise'
        db.delete_column(u'chinesetool_wordplexercise', 'exercise_id')


        # User chose to not deal with backwards NULL issues for 'SentenceZHExercise.exercise_common'
        raise RuntimeError("Cannot reverse this migration. 'SentenceZHExercise.exercise_common' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SentenceZHExercise.exercise_common'
        db.add_column(u'chinesetool_sentencezhexercise', 'exercise_common',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'SentenceZHExercise.exercise'
        db.delete_column(u'chinesetool_sentencezhexercise', 'exercise_id')


        # User chose to not deal with backwards NULL issues for 'WordZHExercise.exercise_common'
        raise RuntimeError("Cannot reverse this migration. 'WordZHExercise.exercise_common' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'WordZHExercise.exercise_common'
        db.add_column(u'chinesetool_wordzhexercise', 'exercise_common',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'WordZHExercise.exercise'
        db.delete_column(u'chinesetool_wordzhexercise', 'exercise_id')


        # User chose to not deal with backwards NULL issues for 'ExplanationExercise.exercise_common'
        raise RuntimeError("Cannot reverse this migration. 'ExplanationExercise.exercise_common' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ExplanationExercise.exercise_common'
        db.add_column(u'chinesetool_explanationexercise', 'exercise_common',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'ExplanationExercise.exercise'
        db.delete_column(u'chinesetool_explanationexercise', 'exercise_id')


        # User chose to not deal with backwards NULL issues for 'SentencePLExercise.exercise_common'
        raise RuntimeError("Cannot reverse this migration. 'SentencePLExercise.exercise_common' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SentencePLExercise.exercise_common'
        db.add_column(u'chinesetool_sentenceplexercise', 'exercise_common',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chinesetool.Exercise']),
                      keep_default=False)

        # Deleting field 'SentencePLExercise.exercise'
        db.delete_column(u'chinesetool_sentenceplexercise', 'exercise_id')


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
        u'chinesetool.exerciseaction': {
            'Meta': {'object_name': 'ExerciseAction'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson_action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.LessonAction']"}),
            'result': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'chinesetool.exercisecommon': {
            'Meta': {'object_name': 'ExerciseCommon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.Lesson']"}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseType']"})
        },
        u'chinesetool.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'NO-DESC'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'NO-NAME'", 'max_length': '20'})
        },
        u'chinesetool.explanationexercise': {
            'Meta': {'object_name': 'ExplanationExercise'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
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
        u'chinesetool.sentenceplexercise': {
            'Meta': {'object_name': 'SentencePLExercise'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
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
        u'chinesetool.sentencezhexercise': {
            'Meta': {'object_name': 'SentenceZHExercise'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
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
        u'chinesetool.wordplexercise': {
            'Meta': {'object_name': 'WordPLExercise'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
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
        u'chinesetool.wordzhexercise': {
            'Meta': {'object_name': 'WordZHExercise'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chinesetool.ExerciseCommon']"}),
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