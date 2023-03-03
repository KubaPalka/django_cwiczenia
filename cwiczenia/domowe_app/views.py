from django.shortcuts import render
from domowe_app.models import Movie


def show_movies(request):
    context = {
        'result': list(Movie.objects.all().order_by('year'))
    }
    return render(request, "domowe_app/movies.html", context)

def show_details(request, id):
    context = {
        'result': Movie.objects.get(pk=id)
    }
    return render(request, "domowe_app/movie_details.html", context)
