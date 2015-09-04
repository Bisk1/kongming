# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessText',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=2)),
                ('translations', models.ManyToManyField(to='translations.BusinessText', related_name='translations_rel_+')),
            ],
        ),
        migrations.CreateModel(
            name='WordPL',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('word', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WordTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('word_pl', models.ForeignKey(to='translations.WordPL')),
            ],
        ),
        migrations.CreateModel(
            name='WordZH',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('word', models.CharField(max_length=50)),
                ('pinyin', models.CharField(max_length=100)),
                ('wordpl_set', models.ManyToManyField(to='translations.WordPL', through='translations.WordTranslation')),
            ],
        ),
        migrations.AddField(
            model_name='wordtranslation',
            name='word_zh',
            field=models.ForeignKey(to='translations.WordZH'),
        ),
        migrations.AlterUniqueTogether(
            name='wordzh',
            unique_together=set([('word', 'pinyin')]),
        ),
        migrations.AlterUniqueTogether(
            name='wordtranslation',
            unique_together=set([('word_zh', 'word_pl')]),
        ),
        migrations.AlterUniqueTogether(
            name='businesstext',
            unique_together=set([('text', 'language')]),
        ),
    ]
