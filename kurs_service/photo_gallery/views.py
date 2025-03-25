from django.http import HttpResponse
from django.shortcuts import render


def photo_gallery(request):
    context = {
        'title': 'Фото-галерея | OOO &quot;КУРС&quot;',
    }
    return render(request, "photo_gallery/photo_gallery.html", context=context)
