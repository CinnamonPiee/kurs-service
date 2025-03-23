from django.http import HttpResponse
from django.shortcuts import render


def site_signup(request):
    return HttpResponse("Site signup page")
