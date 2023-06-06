from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puppies/', views.puppy_index, name='puppy-index'),
  path('puppies/<int:puppy_id>/', views.puppy_detail, name='puppy-detail'),
]