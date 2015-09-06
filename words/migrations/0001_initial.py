# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordPL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('word', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WordZH',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('word', models.CharField(max_length=50)),
                ('pinyin', models.CharField(max_length=100)),
                ('wordpl_set', models.ManyToManyField(to='words.WordPL')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wordzh',
            unique_together=set([('word', 'pinyin')]),
        ),
    ]
