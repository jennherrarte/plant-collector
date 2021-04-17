from django.shortcuts import render
from .models import Plant
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .plant_class import plants

# Define the home view
def home(request):
    return HttpResponse('<h1>Home!</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    context = {
    'plant': plant
    }
    return render(request, 'plants/detail.html', {'plant': plant})

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['name', 'origin', 'description']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'