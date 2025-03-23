from django.http import HttpResponse
from django.shortcuts import render


def online_appointment(request):
    return HttpResponse("Online appointment page")
