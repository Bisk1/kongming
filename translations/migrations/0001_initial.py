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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=2)),
                ('translations', models.ManyToManyField(to='translations.BusinessText', related_name='translations_rel_+')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='businesstext',
            unique_together=set([('text', 'language')]),
        ),
    ]
