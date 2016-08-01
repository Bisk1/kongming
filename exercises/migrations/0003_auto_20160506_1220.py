# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_listening'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explanation',
            name='text',
            field=redactor.fields.RedactorField(),
        ),
    ]
