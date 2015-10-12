# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explanation',
            name='image',
        ),
        migrations.AlterField(
            model_name='explanation',
            name='text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
