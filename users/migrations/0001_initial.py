# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('registration_date', models.DateTimeField()),
                ('last_login_date', models.DateTimeField()),
                ('abo_date', models.DateTimeField()),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WordSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('last_time', models.DateTimeField()),
                ('correct', models.IntegerField(default=0)),
                ('correct_run', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('word_zh', models.ForeignKey(to='translations.WordZH')),
            ],
        ),
    ]
