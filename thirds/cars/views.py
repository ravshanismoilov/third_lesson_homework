from django.shortcuts import render
from .models import Make, Car


def get_make(request):
    makes = Make.objects.all()
    context = {
        'makes': makes
    }
    return render(request, 'home.html', context=context)

def get_car(request, pk):
    cars = Car.objects.filter(category=pk)
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context=context)

def get_detail(request, pk):
    info = Car.objects.get(pk=pk)
    context = {
        'info': info
    }
    return render(request, 'detail.html', context=context)