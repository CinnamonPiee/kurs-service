from django.http import HttpResponse
from django.shortcuts import render


def diagnostics(request):
    return HttpResponse("Diagnostics page")
