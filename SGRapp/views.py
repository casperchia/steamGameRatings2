from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Game
import steamapi
from steamGameRatings.settings import STEAM_API_KEY
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    # games_list = Game.objects.all()
    context = {
        # 'games_list': games_list
    }
    return render(request, 'SGRapp/index.html', context)


def results(request, steamId=None, steamName=None):
    steamapi.core.APIConnection(api_key=STEAM_API_KEY)
    # need to try and catch error here:
    user = steamapi.user.SteamUser(userid=steamId, userurl=steamName)
    games = []
    for game in user.games:
        try:
            games.append(Game.objects.get(pk=game.id))
        except ObjectDoesNotExist:
            print(str(game.id) + " does not exist in db.")
    context = {
        'steamName': user.name,
        'steamId': user.id,
        'steamLevel': user.level,
        'steamUrl': user.profile_url,
        'privacy': user.privacy,
        'games': games,
        'avatarImg': user.avatar_full,
    }
    return render(request, 'SGRapp/results.html', context)


def goto(request):
    userInput = request.GET.get('userInput', '')
    if request.GET.get('inputType') == 'steamName':
        return HttpResponseRedirect('/username/' + userInput)
    else:
        return HttpResponseRedirect('/id/' + userInput)
