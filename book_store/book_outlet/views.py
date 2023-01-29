from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("raiting")
    total_number_of_books = books.count()
    average_raiting = books.aggregate(Avg("raiting"))

    context = {
        "books": books,
        "total_number_of_books": total_number_of_books,
        "average_raiting": average_raiting
    }

    return render(request, "book_outlet/index.html", context)

# def book_detail(request, id):
def book_detail(request, slug):
    # book = get_object_or_404(Book, pk = id)
    book = get_object_or_404(Book, slug = slug)
    context = {
        "title": book.title,
        "author": book.author,
        "raiting": book.raiting,
        "is_bestseller": book.is_bestselling
    }

    return render(request, "book_outlet/book_detail.html", context)