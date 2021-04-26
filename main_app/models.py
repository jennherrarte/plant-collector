from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# import your models here

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Pot(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.name} {self.color}'

    # Add this method
  def get_absolute_url(self):
    return reverse('pot_detail', kwargs={'pot_id': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=255) 
    pots = models.ManyToManyField(Pot)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
      return self.name
    
  # Add this method
    def get_absolute_url(self):
      return reverse('detail', kwargs={'plant_id': self.id})

    

class Watering(models.Model):
  date = models.DateField('Watering Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0])
    
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
  def __str__(self): 
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']



class Photo(models.Model):
    url = models.CharField(max_length=200)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for plant_id: {self.plant_id} @{self.url}"

