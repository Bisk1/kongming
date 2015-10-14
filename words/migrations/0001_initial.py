# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordEN',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('word', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WordZH',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('word', models.CharField(max_length=50)),
                ('pinyin', models.CharField(max_length=100)),
                ('worden_set', models.ManyToManyField(to='words.WordEN')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wordzh',
            unique_together=set([('word', 'pinyin')]),
        ),
    ]
