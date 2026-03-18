from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Review
from book.models import Book

class ReviewForm(forms.Form):
    reviewer_name = forms.CharField(max_length=100)
    rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = forms.CharField(widget=forms.Textarea)