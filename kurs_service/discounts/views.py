from django.http import HttpResponse
from django.shortcuts import render


def discounts(request):
    context = {
        'title': 'Акции | OOO &quot;КУРС&quot;',
    }
    return render(request, "discounts/discounts.html", context=context)
