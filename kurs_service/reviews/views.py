from django.http import HttpResponse
from django.shortcuts import render


def reviews(request):
    context = {
        'title': 'Отзывы | OOO "КУРС"',
    }
    return render(request, "reviews/reviews.html", context=context)
