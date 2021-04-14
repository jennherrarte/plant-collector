from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .plant_class import plants

# Define the home view
def home(request):
  return HttpResponse('<h1>Home!</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', { 'plants': plants })