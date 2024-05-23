from django.db import models
from .helper import Helper


class Column(models.Model):
  name = models.CharField(max_length=100)
  td = models.IntegerField(choices=Helper.TD_CHOICES, null=True)
  content = models.CharField(max_length=1024)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
