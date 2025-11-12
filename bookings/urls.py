from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/', views.book_tour, name='book_tour'),
]
