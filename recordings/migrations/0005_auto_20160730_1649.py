# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0004_auto_20160730_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='explanation',
            field=models.ForeignKey(to='exercises.Explanation'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='link_id',
            field=models.CharField(max_length=20),
        ),
    ]
