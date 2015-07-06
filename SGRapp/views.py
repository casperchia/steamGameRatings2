from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Game
import steamapi
from steamGameRatings.settings import STEAM_API_KEY


def index(request):
    # games_list = Game.objects.all()
    context = {
        # 'games_list': games_list
    }
    return render(request, 'SGRapp/index.html', context)


def results(request, steamId=None, steamName=None):
    steamapi.core.APIConnection(api_key=STEAM_API_KEY)
    if steamId is not None:
        user = steamapi.user.SteamUser(steamId)

    if steamName is not None:
        user = steamapi.user.SteamUser(userurl=steamName)

    context = {
        'steamName': user.name,
        'steamId': user.id,
        'games': user.games,
        'avatarImg': user.avatar_medium,
    }
    return render(request, 'SGRapp/results.html', context)


def goto(request):
    userInput = request.GET.get('userInput', '')
    if request.GET.get('inputType') == 'steamName':
        return HttpResponseRedirect('/username/' + userInput)
    else:
        return HttpResponseRedirect('/id/' + userInput)
