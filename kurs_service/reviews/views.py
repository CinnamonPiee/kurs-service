from django.http import HttpResponse
from django.shortcuts import render


def reviews(request):
    return HttpResponse("Reviews page")
