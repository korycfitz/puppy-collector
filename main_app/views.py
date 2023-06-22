from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Puppy

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('puppy-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

@login_required
def puppy_index(request):
  puppies = Puppy.objects.filter(user=request.user)
  return render(request, 'puppies/index.html', { 'puppies': puppies })

@login_required
def puppy_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy })

class PuppyCreate(LoginRequiredMixin, CreateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/puppies/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    return super().form_valid(form)

class PuppyUpdate(LoginRequiredMixin, UpdateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']

class PuppyDelete(LoginRequiredMixin, DeleteView):
  model = Puppy
  success_url = '/puppies/'

