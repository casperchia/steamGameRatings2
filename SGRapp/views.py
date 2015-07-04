from django.shortcuts import render


def index(request):
    numList = range(1, 10)
    context = {
        'numList': numList
    }
    return render(request, 'SGRapp/index.html', context)
