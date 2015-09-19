# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstext',
            name='words_pl',
            field=models.ManyToManyField(to='words.WordPL'),
        ),
        migrations.AddField(
            model_name='businesstext',
            name='words_zh',
            field=models.ManyToManyField(to='words.WordZH'),
        ),
    ]
