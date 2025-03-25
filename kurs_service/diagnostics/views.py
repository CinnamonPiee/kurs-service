from django.http import HttpResponse
from django.shortcuts import render


def diagnostics(request):
    context = {
        'title': 'Диагностика | OOO &quot;КУРС&quot;',
    }
    return render(request, "diagnostics/diagnostics.html", context=context)
