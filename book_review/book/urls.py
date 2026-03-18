from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book-details/<int:book_pk>/', views.book_details, name='book_details'),
    path('add-review/<int:book_pk>', views.add_review, name='add_review'),
]