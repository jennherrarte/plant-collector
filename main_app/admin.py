from django.contrib import admin
# import your models here
from .models import Plant, Watering

# Register your models here
admin.site.register(Plant)
admin.site.register(Watering)