from django.db import models


class Lesson(models.Model):
    topic = models.CharField(max_length=100)
    exercises_number = models.PositiveIntegerField()
    requirement = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return self.topic