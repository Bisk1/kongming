# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20160506_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioPlaceholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('link_id', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=20)),
                ('explanation', models.ForeignKey(to='exercises.Explanation')),
            ],
        ),
    ]
