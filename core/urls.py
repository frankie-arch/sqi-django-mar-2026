from django.urls import path
from . import views

app_name = "core" 

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
]