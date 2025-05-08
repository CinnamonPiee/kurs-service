from django.shortcuts import render
from .models import (
	MainPageSliderImages,
    MainPageTitles,
    MainPageDirectionOfActivity,
)
from about.models import AboutOurAdvantages


def main_page(request):
     context = {
        'title': 'Главная страница | OOO "КУРС"',
        'main_page_slider_images': MainPageSliderImages.objects.all(),
        'about_our_advantages': AboutOurAdvantages.objects.all(),
        'main_page_direction_of_activity': MainPageDirectionOfActivity.objects.all(),
        'main_page_titles': MainPageTitles.objects.first(),
     }
     return render(request, "main_page/main_page.html", context=context)
