from django.shortcuts import render
from .models import Category, Author, Language, Book


def get_info(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    context = {
        'categories': categories,
        'authors': authors
    }
    return render(request, 'home.html', context=context)

def get_books(request, pk):
    products = Book.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'product.html', context=context)

def get_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context=context)