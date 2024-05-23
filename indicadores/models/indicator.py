from django.db import models
from .helper import Helper


class Indicator(models.Model):
  area_id = models.ForeignKey('Area', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  indicator_url = models.CharField(max_length=200)
  indicator_visible = models.BooleanField(default=True)
  indicator_order = models.IntegerField(default=0)
  status = models.IntegerField(choices=Helper.STATUS_CHOICES, default=1)
  responsible = models.IntegerField(choices=Helper.RESPONSIBLE_CHOICES, default=1)
  table_info = models.CharField(max_length=256)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class Indicator1(models.Model):
  period = models.IntegerField(choices=Helper.PERIOD_CHOICES, default=1)
  column_a_general_text = models.CharField(max_length=50)
  column_b_first_data = models.CharField(max_length=50)
  column_c_second_data = models.CharField(max_length=50)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
