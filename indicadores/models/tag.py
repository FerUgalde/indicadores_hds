from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=50)
  tags = models.CharField(max_length=200)
  area_id = models.ForeignKey('Area', on_delete=models.CASCADE)
  indicator_id = models.ForeignKey('Indicator', on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class TagN(models.Model):
  name = models.CharField(max_length=256)
  idfc = models.CharField(max_length=512)
  ca = models.CharField(max_length=512)

  area_id = models.ForeignKey('Area', on_delete=models.CASCADE)
  indicator_id = models.ForeignKey('Indicator', on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
