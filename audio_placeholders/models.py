from django.db import models
from exercises.models import Explanation


class AudioPlaceholder(models.Model):
    link_id = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    explanation = models.ForeignKey(Explanation)

    def __str__(self):
        return self.text
