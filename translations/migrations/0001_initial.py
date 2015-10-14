# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessText',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=2)),
                ('translations', models.ManyToManyField(related_name='translations_rel_+', to='translations.BusinessText')),
                ('words_en', models.ManyToManyField(to='words.WordEN')),
                ('words_zh', models.ManyToManyField(to='words.WordZH')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='businesstext',
            unique_together=set([('text', 'language')]),
        ),
    ]
