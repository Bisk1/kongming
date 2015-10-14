# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('number', models.IntegerField(null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(auto_created=True, to='exercises.AbstractExercise', serialize=False, parent_link=True, primary_key=True)),
                ('correct_choice', models.ForeignKey(to='translations.BusinessText', related_name='choice_exercise_as_correct')),
                ('text_to_translate', models.ForeignKey(to='translations.BusinessText', related_name='choice_exercise_as_text_to_translate')),
                ('wrong_choices', models.ManyToManyField(related_name='choice_exercise_as_wrong', to='translations.BusinessText')),
            ],
            bases=('exercises.abstractexercise',),
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(auto_created=True, to='exercises.AbstractExercise', serialize=False, parent_link=True, primary_key=True)),
                ('text', redactor.fields.RedactorField(verbose_name='Text')),
            ],
            bases=('exercises.abstractexercise',),
        ),
        migrations.CreateModel(
            name='Typing',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(auto_created=True, to='exercises.AbstractExercise', serialize=False, parent_link=True, primary_key=True)),
                ('text_to_translate', models.ForeignKey(to='translations.BusinessText')),
            ],
            bases=('exercises.abstractexercise',),
        ),
    ]
