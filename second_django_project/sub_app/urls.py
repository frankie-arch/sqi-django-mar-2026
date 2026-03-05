from django.urls import path

from . import views

urlpatterns = [
    path('home-page/', views.home_page, name=('home_page')),
    path('home-views/', views.home_views, name="home_views"),
]