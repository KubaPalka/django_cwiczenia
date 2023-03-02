from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def hello(request):
    return HttpResponse("Hello world!")

def random_number(request):
    rnd_num = randint(1, 100)
    return HttpResponse(f"Wylosowana liczba to: {rnd_num}")

def random_from_max(request, max_number):
    max_number = int(max_number)
    rnd_num = randint(1, max_number)
    return HttpResponse(f"Użytkownik podał zakres do {max_number}. Wylosowano: {rnd_num}")

def random_min_max(request, min_number, max_number):
    min_number = int(min_number)
    max_number = int(max_number)
    rnd_number = randint(min_number, max_number)
    return HttpResponse(f"Użytkownik podał zakres od {min_number} do {max_number}. Wylosowane: {rnd_number}")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}!")

def add_values(request, val_1, val_2):
    result = int(val_1) + int(val_2)
    return HttpResponse(f"Wnik dodawania {val_1} i {val_2} to {result}")