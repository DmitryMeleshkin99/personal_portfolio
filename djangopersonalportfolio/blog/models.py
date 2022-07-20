from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, DateTimeField

# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
