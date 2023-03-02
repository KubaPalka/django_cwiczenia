from django.shortcuts import render
from django.http import HttpResponse
from bazy_danych.functions import find_categories
from bazy_danych.models import Category




def categories(request):
    context = {
        'result': find_categories(Category),
    }
    return render(request, "bazy_danych/categories.html", context)

