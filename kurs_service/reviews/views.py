from django.http import HttpResponse
from django.shortcuts import render


def reviews(request):
    context = {
        'title': 'Отзывы | OOO &quot;КУРС&quot;',
    }
    return render(request, "reviews/reviews.html", context=context)
