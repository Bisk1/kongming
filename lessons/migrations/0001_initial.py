# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('topic', models.CharField(max_length=100)),
                ('exercises_number', models.PositiveIntegerField()),
                ('requirement', models.ForeignKey(to='lessons.Lesson', blank=True, null=True)),
            ],
        ),
    ]
