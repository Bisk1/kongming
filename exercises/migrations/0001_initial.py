# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
        ('translations', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('number', models.IntegerField(null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(to='exercises.AbstractExercise', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('text', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='image/')),
            ],
            bases=('exercises.abstractexercise',),
        ),
        migrations.CreateModel(
            name='Typing',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(to='exercises.AbstractExercise', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('text_to_translate', models.ForeignKey(to='translations.BusinessText')),
            ],
            bases=('exercises.abstractexercise',),
        ),
    ]
