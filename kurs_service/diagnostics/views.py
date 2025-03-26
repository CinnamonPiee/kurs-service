from django.http import HttpResponse
from django.shortcuts import render


def diagnostics(request):
    context = {
        'title': 'Диагностика | OOO "КУРС"',
    }
    return render(request, "diagnostics/diagnostics.html", context=context)
