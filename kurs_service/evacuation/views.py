from django.http import HttpResponse
from django.shortcuts import render


def evacuation(request):
    return HttpResponse("Evacuation page")
