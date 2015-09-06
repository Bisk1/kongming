# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseAction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('result', models.CharField(default='u', max_length=1)),
                ('number', models.IntegerField()),
                ('exercise', models.ForeignKey(to='exercises.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='LessonAction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('total_exercises_number', models.IntegerField(default=0)),
                ('current_exercise_number', models.IntegerField(default=0)),
                ('fails', models.IntegerField(default=0)),
                ('status', models.CharField(default=None, max_length=1, null=True)),
                ('lesson', models.ForeignKey(to='lessons.Lesson', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exerciseaction',
            name='lesson_action',
            field=models.ForeignKey(to='learn.LessonAction'),
        ),
    ]
