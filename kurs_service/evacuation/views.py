from django.http import HttpResponse
from django.shortcuts import render


def evacuation(request):
    context = {
        'title': 'Эвакуация | OOO "КУРС"',
    }
    return render(request, "evacuation/evacuation.html", context=context)
