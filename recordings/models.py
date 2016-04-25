from django.db import models


class Recording(models.Model):
    text = models.CharField(max_length=20)
    url = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.text
