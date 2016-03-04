# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonaction',
            name='status',
            field=models.CharField(max_length=1, null=True, default='u'),
        ),
    ]
