from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Puppy

def signup(request):
  error_message = ''
  if request.method == 'POST': #create a 'user' form object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid(): #add the user to the database
      user = form.save() #log a user in
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm() #render signup.html with an empty form on error
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
def puppy_index(request):
  puppies = Puppy.objects.filter(user=request.user)
  return render(request, 'puppies/index.html', { 'puppies': puppies })

def puppy_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy })

class PuppyCreate(CreateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/puppies/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    return super().form_valid(form)

class PuppyUpdate(UpdateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'

