from django.http import HttpResponse
from django.shortcuts import render


def news(request):
    return HttpResponse("News page")
