from django.http import HttpResponse
from django.shortcuts import render


def discounts(request):
    return HttpResponse("Discounts page")
