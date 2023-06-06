from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Puppy

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
def puppy_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', { 'puppies': puppies })

def puppy_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy })

class PuppyCreate(CreateView):
  model = Puppy
  fields = '__all__'
  success_url = '/puppies/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    return super().form_valid(form)

class PuppyUpdate(UpdateView):
  model = Puppy
  fields = '__all__'

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'

