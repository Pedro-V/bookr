from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    context = {
        "site_name": "Bookr"
    }
    return render(request, "base.html", context)

def search_result(request):
    context = {
        "search_term": request.GET.get("search", ""),
    }
    return render(request, "search_result.html", context)

def welcome_view(request):
    message = f"<html>
    <h1>Welcome to Bookr!</h1>
    <p>{Book.objects.count()} books and counting!</p>
    </html>"
    return HttpResponse(message)
