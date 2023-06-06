from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

class Puppy(models.Model):
  name = models.CharField(max_length=50)
  breed = models.CharField(max_length=75)
  description = models.TextField(max_length=300)
  age = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('puppy-detail', kwargs={'puppy_id': self.id})
  