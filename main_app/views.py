from django.shortcuts import render
from .models import Puppy

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def puppy_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', { 'puppies': puppies })

class Puppy:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

puppies = [
  Puppy('Snowball', 'maltese', 'old', 16),
  Puppy('Bailey', 'rut', 'huge', 3),
  Puppy('Bear', 'golden retriever', 'cute', 2),
  Puppy('Cooper', 'german shepherd', 'scary', 10)
]