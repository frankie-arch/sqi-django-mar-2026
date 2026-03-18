from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm

from .models import Review
from book.models import Book
# Create your views here.

# def review(request):
#     return render(request, 'review/review.html', {'reviews':Review.objects.all()})


