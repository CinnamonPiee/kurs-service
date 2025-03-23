from django.http import HttpResponse
from django.shortcuts import render


def check_list(request):
    return HttpResponse("Check list page")
