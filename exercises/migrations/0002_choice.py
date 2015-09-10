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
            name='Choice',
            fields=[
                ('abstractexercise_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, serialize=False, to='exercises.AbstractExercise')),
                ('correct_choice', models.ForeignKey(related_name='choice_exercise_as_correct', to='translations.BusinessText')),
                ('text_to_translate', models.ForeignKey(related_name='choice_exercise_as_text_to_translate', to='translations.BusinessText')),
                ('wrong_choices', models.ManyToManyField(related_name='choice_exercise_as_wrong', to='translations.BusinessText')),
            ],
            bases=('exercises.abstractexercise',),
        ),
    ]
