from django.shortcuts import render, redirect
from django.http import HttpResponse
# generic CBV's
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Our Models
from .models import Plant, Photo, Pot
from .forms import WateringForm
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector17'

# Define the home view
def home(request):
    return HttpResponse('<h1>Home!</h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
  # You could also retrieve the logged in user's cats like this
  # cats = request.user.cat_set.all()
    return render(request, 'plants/index.html', { 'plants': plants })

    return render(request, 'plants/index.html', { 'plants': plants })

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    pots_plant_doesnt_have = Pot.objects.exclude(id__in = plant.pots.all().values_list('id'))
    watering_form = WateringForm()
    context = {
      'plant': plant,
      'watering_form': watering_form,
      'pots': pots_plant_doesnt_have
    }
    return render(request, 'plants/detail.html', context)

@login_required
def add_watering(request, plant_id):
  form = WateringForm(request.POST)

  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
    return redirect('detail', plant_id=plant_id)



class PlantCreate(LoginRequiredMixin, CreateView):
  model = Plant
  fields = '__all__'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
  model = Plant
  fields = ['name', 'origin', 'description']

class PlantDelete(LoginRequiredMixin, DeleteView):
  model = Plant
  success_url = '/plants/'

@login_required
def add_photo(request, plant_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to plant_id or plant (if you have a plant object)
      photo = Photo(url=url, plant_id=plant_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
    return redirect('detail', plant_id=plant_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




@login_required
def pots_index(request):
    pots = Pot.objects.all()
    context = {'pots': pots}

    return render(request, 'pot/index.html', context)


@login_required
def pot_detail(request, pot_id):
    pot = Pot.objects.get(id=pot_id)
    context = {
        'pot': pot
    }
    return render(request, 'pot/detail.html', context)

@login_required
def assoc_pot(request, plant_id, pot_id):
  Plant.objects.get(id=plant_id).pots.add(pot_id)
  return redirect('detail', plant_id=plant_id)


@login_required
def remove_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id=plant_id)

class Create_Pot(LoginRequiredMixin, CreateView):
    model = Pot
    fields = '__all__'


class Update_pot(LoginRequiredMixin, UpdateView):
    model = Pot
    fields = ['color']


class Delete_pot(LoginRequiredMixin, DeleteView):
    model = Pot
    success_url = '/pots/'






