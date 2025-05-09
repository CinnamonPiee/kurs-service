from django.shortcuts import render
from .models import (
	MainPageSliderImages,
	MainPageTitles,
	MainPageDirectionOfActivity,
	MainPageAlwaysInStock,
	MainPageAdditionalPowerEquipmentAMZ,
	MainPageAdditionalPowerEquipment,
	MainPageEverythingToBeConsideredTheBest,
	MainPageFrequentlyAskedQuestions,
	MainPageOurAdvantages,
	MainPageProfessionalEquipment
)
from about.models import AboutOurAdvantages


def main_page(request):
     context = {
        'title': 'Главная страница | OOO "КУРС"',
        'main_page_slider_images': MainPageSliderImages.objects.all(),
        'about_our_advantages': AboutOurAdvantages.objects.all(),
        'main_page_direction_of_activity': MainPageDirectionOfActivity.objects.all(),
        'main_page_titles': MainPageTitles.objects.first(),
        'main_page_always_in_stock': MainPageAlwaysInStock.objects.all(),
        'main_page_additional_power_equipment': MainPageAdditionalPowerEquipment.objects.all(),
        'main_page_additional_power_equipment_amz': MainPageAdditionalPowerEquipmentAMZ.objects.first(),
        'main_page_everything_to_be_considered_the_best_first_four': MainPageEverythingToBeConsideredTheBest.objects.all()[:4],
        'main_page_everything_to_be_considered_the_best_last_four': MainPageEverythingToBeConsideredTheBest.objects.all()[4:],
        'main_page_frequently_asked_questions': MainPageFrequentlyAskedQuestions.objects.all(),
        'main_page_our_advantages': MainPageOurAdvantages.objects.first(),
        'main_page_professional_equipment': MainPageProfessionalEquipment.objects.all(),
     }
     return render(request, "main_page/main_page.html", context=context)
