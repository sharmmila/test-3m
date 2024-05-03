from django.shortcuts import render

from film.models import Film, Actor, Genre
from django.shortcuts import HttpResponse

def main_view(request):
    return render(request, "main.html")


def list_films_view(request):
    films = Film.objects.all()
    return render(request, "films/list.html", {"films": films})


def film_detail_view(request, film_id):
    if request.method == 'GET':
        try:
            film = Film.objects.get(id=film_id)
        except Film.DoesNotExist:
            return HttpResponse('Film not found', status=404)

        context = {'film': film}

        return render(request, 'films/film_detail.html', context)