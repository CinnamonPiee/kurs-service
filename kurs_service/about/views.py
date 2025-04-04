from django.shortcuts import render
from about.models import (
    AboutImages,
    AboutDescriptionCompany,
    AboutAdvantages,
    AboutContacts,
    AboutTrainingStaff,
	AboutTitles,
)


def about(request):
    context = {
        'title': 'О сервисе | OOO "КУРС"',
        'about_images_best_in_business': AboutImages.objects.first(),
        'about_images_in_time': AboutImages.objects.last(),
        'about_description_company': AboutDescriptionCompany.objects.first(),
        'about_advantages': AboutAdvantages.objects.all(),
        'about_contacts': AboutContacts.objects.all(),
        'about_training_staff': AboutTrainingStaff.objects.all(),
        'about_titles': AboutTitles.objects.first(),
    }
    return render(request, "about/about.html", context=context)
