from django.contrib.auth.models import User
from django.db import models
from words.models import WordZH


class Subscription(models.Model):
    name = models.ForeignKey(User)
    registration_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    abo_date = models.DateTimeField()

    def __str__(self):
        return self.name


class WordSkill(models.Model):
    word_zh = models.ForeignKey(WordZH)
    user = models.ForeignKey(User)
    last_time = models.DateTimeField()
    correct = models.IntegerField(default=0)
    correct_run = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)