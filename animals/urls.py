from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('', views.animal_list, name='list'),
    path('<int:pk>/', views.animal_detail, name='detail'),
    path('today/', views.animal_of_the_day, name='today'),
    path('next/', views.next_animal_collection, name='next_collection'),
    
]
