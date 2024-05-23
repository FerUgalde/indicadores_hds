from django.db import models
from .helper import Helper

class Area(models.Model):
  name = models.CharField(max_length=100)
  icon = models.CharField(max_length=100)
  status = models.IntegerField(choices=Helper.STATUS_CHOICES, default=1)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class AccessArea(models.Model):
  is_active = models.BooleanField(default=True)

  user_id = models.ForeignKey('User', on_delete=models.CASCADE)
  area_id = models.ForeignKey('Area', on_delete=models.CASCADE)
  indicatior_id = models.ForeignKey('Indicator', on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.name
