from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

from review.models import Review
from review.forms import ReviewForm

# Create your views here.

def book_list(request):
    return render(request, 'book/book-list.html', {'book_list': Book.objects.all()})

def book_details(request, book_pk):
    return render(request, 'book/book-details.html', {'book_details': get_object_or_404(Book, pk=book_pk), 'reviews': Review.objects.filter(book=book_pk)})

def add_review(request, book_pk):

    book = get_object_or_404(Book, pk=book_pk)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            Review.objects.create(
                book=book,
                reviewer_name=data['reviewer_name'],
                rating=data['rating'],
                comment=data['comment']
            )

            return redirect('book:book_details', book_pk)

        

    return render(request, 'review/add-review.html', {'form': form,'book': book})