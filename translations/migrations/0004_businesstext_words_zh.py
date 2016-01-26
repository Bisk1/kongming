# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
        ('translations', '0003_remove_businesstext_words_zh'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstext',
            name='words_zh',
            field=models.ManyToManyField(through='translations.BusinessTextWordZH', to='words.WordZH'),
        ),
    ]
