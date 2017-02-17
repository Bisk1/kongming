# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20160730_1644'),
        ('recordings', '0003_auto_20160420_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='url',
        ),
        migrations.AddField(
            model_name='recording',
            name='explanation',
            field=models.ForeignKey(null=True, to='exercises.Explanation'),
        ),
        migrations.AddField(
            model_name='recording',
            name='link_id',
            field=models.CharField(null=True, max_length=20),
        ),
    ]
