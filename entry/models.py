from uuid import uuid4
from django.db import models
from django.conf import settings


# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} {self.body}"


class NotePad(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.PROTECT)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
