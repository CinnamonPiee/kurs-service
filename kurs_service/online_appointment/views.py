from django.http import HttpResponse
from django.shortcuts import render


def online_appointment(request):
    context = {
        'title': 'Онлайн запись | OOO &quot;КУРС&quot;',
    }
    return render(request, "online_appointment/online_appointment.html", context=context)
