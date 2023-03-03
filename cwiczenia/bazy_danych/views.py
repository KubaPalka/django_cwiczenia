from django.shortcuts import render
from django.http import HttpResponse
from bazy_danych.functions import find_categories
from bazy_danych.models import Category, Band




def categories(request):
    context = {
        'result': find_categories(Category),
    }
    return render(request, "bazy_danych/categories.html", context)

def show_band(request, id):
    context = {
        'result': Band.objects.get(pk=id)
    }
    return render(request, "bazy_danych/show.html", context)





