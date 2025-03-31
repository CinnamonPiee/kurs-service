from django.shortcuts import render
from contacts.models import DrivingDirection


def contacts(request):
    context = {
        'title': 'Контакты | OOO "КУРС"',
        'img_and_text': DrivingDirection.objects.all(),
    }
    return render(request, "contacts/contacts.html", context=context)
