from django.db import models

class Puppy(models.Model):
  name = models.CharField(max_length=50)
  breed = models.CharField(max_length=75)
  description = models.TextField(max_length=300)
  age = models.IntegerField()

  def __str__(self):
    return self.name