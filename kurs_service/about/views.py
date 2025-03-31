from django.shortcuts import render
from about.models import Training, DescriptionCompany


def about(request):
    context = {
        'title': 'О сервисе | OOO "КУРС"',
        'training_img': Training.objects.all(),
        'about_text': DescriptionCompany.objects.last(),
    }
    return render(request, "about/about.html", context=context)
