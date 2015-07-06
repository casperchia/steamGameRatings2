from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Game
import steamapi


def index(request):
    # games_list = Game.objects.all()
    context = {
        # 'games_list': games_list
    }
    return render(request, 'SGRapp/index.html', context)


def results(request, steamId=None, steamName=None):
    if steamId is not None:
        context = {
            'username': steamId
        }
    if steamName is not None:
        context = {
            'username': steamName
        }
    return render(request, 'SGRapp/results.html', context)


def goto(request):
    userInput = request.GET.get('userInput', '')
    if request.GET.get('inputType') == 'steamName':
        return HttpResponseRedirect('/username/' + userInput)
    else:
        return HttpResponseRedirect('/id/' + userInput)
