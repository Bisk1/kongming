# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTextWordZH',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ordinal', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='businesstext',
            name='words_en',
        ),
        migrations.AddField(
            model_name='businesstextwordzh',
            name='text',
            field=models.ForeignKey(to='translations.BusinessText'),
        ),
        migrations.AddField(
            model_name='businesstextwordzh',
            name='word',
            field=models.ForeignKey(to='words.WordZH'),
        ),
    ]
