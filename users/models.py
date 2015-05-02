from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    name = models.ForeignKey(User)
    registration_date = models.DateTimeField()
    last_login_date = models.DateTimeField()
    abo_date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.name)

