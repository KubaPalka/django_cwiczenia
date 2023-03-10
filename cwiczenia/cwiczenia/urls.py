"""cwiczenia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dzien1.views import hello, random_number, random_from_max, random_min_max, hello_name, add_values
from bazy_danych.views import categories, show_band
from domowe_app.views import show_movies, show_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('random/', random_number),
    path('random/<max_number>/', random_from_max),
    path('random/<min_number>/<max_number>/', random_min_max),
    path('hello/<name>/', hello_name),
    path('add/<val_1>/<val_2>/', add_values),
    path('categories/', categories),
    path('show-band/<int:id>/', show_band),
    path('movies/', show_movies),
    path('movie-details/<id>', show_details),
]
