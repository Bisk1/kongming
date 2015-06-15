from django.db import models


class Lesson(models.Model):
    """
    Single Chinese lesson is defined by level
    and words related to it.
    """
    topic = models.CharField(max_length=100, default="NO-NAME")
    exercises_number = models.IntegerField()
    requirement = models.ForeignKey("self", null=True)

    def __unicode__(self):
        return unicode(self.topic)

