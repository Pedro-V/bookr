from django.shortcuts import render, get_object_or_404

from .models import Book
from .utils import average_rating

def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    context = {
        "search_text": search_text,
    }
    return render(request, "search_results.html", context)


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list.html', context)

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.review_set.all()

    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
    else:
        book_rating = None

    context = {
        "book": book,
        "book_rating": book_rating,
        "reviews": reviews,
    }
    return render(request, "book_details.html", context)

