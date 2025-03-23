from django.http import HttpResponse
from django.shortcuts import render


def photo_gallery(request):
    return HttpResponse("Photo gallery page")
