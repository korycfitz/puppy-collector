from django.db import models
from django.urls import reverse

class Puppy(models.Model):
  name = models.CharField(max_length=50)
  breed = models.CharField(max_length=75)
  description = models.TextField(max_length=300)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('puppy-detail', kwargs={'puppy_id': self.id})