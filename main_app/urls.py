from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('plants/<int:plant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pots/', views.pots_index, name='pots_index'),
    path('pots/<int:pot_id>/', views.pot_detail, name='pot_detail'),
    path('pots/create/', views.Create_Pot.as_view(), name='create_pot'),
    path('pots/<int:pk>/update/', views.Update_pot.as_view(), name='update_pot'),
    path('plants/<int:plant_id>/assoc_pot/<int:pot_id>/', views.assoc_pot, name='assoc_pot'),
    path('pots/<int:pk>/delete/', views.Delete_pot.as_view(), name='delete_pot'),
  

]



  

