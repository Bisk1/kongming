# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0001_initial'),
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(to='exercises.AbstractExercise', primary_key=True, serialize=False, auto_created=True, parent_link=True)),
                ('audio', models.FileField(upload_to='wav')),
                ('text', models.ForeignKey(to='translations.BusinessText')),
            ],
            bases=('exercises.abstractexercise',),
        ),
    ]
