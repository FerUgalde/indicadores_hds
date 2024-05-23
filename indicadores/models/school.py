from django.db import models
from .helper import Helper


class BachelorProgramInfo(models.Model):
  name = models.CharField(max_length=100)
  period = models.IntegerField(choices=Helper.PERIOD_CHOICES, null=True)
  num_students_male = models.IntegerField(default=0)
  num_students_female = models.IntegerField(default=0)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class ProfessionalPractice(models.Model):
  name = models.CharField(max_length=100)
  period = models.IntegerField(choices=Helper.PERIOD_CHOICES, null=True)
  num_student_male = models.IntegerField(default=0)
  num_student_female = models.IntegerField(default=0)

  bachelor_program_info = models.ForeignKey('BachelorProgramInfo', on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Pvvc(models.Model):
  name = models.CharField(max_length=100, default='PVVC')
  period = models.IntegerField(choices=Helper.PERIOD_CHOICES, null=True)
  BachelorProgramInfo = models.ForeignKey('BachelorProgramInfo', on_delete=models.CASCADE)
  num_students_male = models.IntegerField(default=0)
  num_students_female = models.IntegerField(default=0)
  qty_projects = models.IntegerField(default=0)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.name
