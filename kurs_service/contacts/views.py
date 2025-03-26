from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    context = {
        'title': 'Контакты | OOO "КУРС"',
    }
    return render(request, "contacts/contacts.html", context=context)
