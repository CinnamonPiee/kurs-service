from django.http import HttpResponse
from django.shortcuts import render


def check_list(request):
    context = {
        'title': 'Чен лист | OOO &quot;КУРС&quot;',
    }
    return render(request, "check_list/check_list.html", context=context)
