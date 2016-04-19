# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0002_auto_20160420_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recording',
            old_name='name',
            new_name='text',
        ),
    ]
