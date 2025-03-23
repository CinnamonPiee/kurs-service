from django.http import HttpResponse
from django.shortcuts import render


def warranty(request):
    return HttpResponse("Warranty page")
