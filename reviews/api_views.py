from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book

@api_view()
def book_amount(request):
    num_books = Book.objects.count()
    return Response({'num_books': num_books}) 

