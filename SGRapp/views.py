from django.shortcuts import render
from .models import Game


def index(request):
    games_list = Game.objects.all()
    context = {
        'games_list': games_list
    }
    return render(request, 'SGRapp/index.html', context)
