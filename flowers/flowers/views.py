from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from .forms import *


def index(request: WSGIRequest):
    flowers = Flowers.objects.filter(published=True)
    context = {
        'flowers': flowers
    }

    return render(request, 'index.html', context)


def category(request: WSGIRequest, type_id):
    type = get_object_or_404(Categories, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)
    context = {
        'types': [type],
        'flowers': flowers
    }

    return render(request, 'index.html', context)


def flower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower
    }
    return render(request, 'detail.html', context)


def add_species(request):
    if request.method == 'POST':
        form = CategoriesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            species = Categories.objects.create(**form.cleaned_data)
            print(species, "qo'shildi!")

    form = CategoriesForm()
    context = {
        'form': form,
        'title': "O'simlik turi qo'shish"
    }
    return render(request, 'add_species.html', context)


def add_flowers(request):
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flowers = Flowers.objects.create(**form.cleaned_data)
            print(flowers, "qo'shildi!")

    form = FlowerForm()
    context = {
        'form': form,
        'title': "Gul qo'shish"
    }
    return render(request, 'add_flowers.html', context)
