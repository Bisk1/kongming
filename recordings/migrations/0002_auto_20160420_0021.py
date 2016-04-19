# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recording',
            name='url',
            field=models.CharField(null=True, max_length=40),
        ),
    ]
