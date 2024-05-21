from django.shortcuts import render
from .models import Category, Products


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'home.html', context=context)

def get_products(request, pk):
    products = Products.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)

def get_detail(request, pk):
    p = Products.objects.get(pk=pk)
    context = {
        'p': p
    }
    return render(request, 'detail.html', context=context)