# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0002_auto_20160125_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesstext',
            name='words_zh',
        ),
    ]
