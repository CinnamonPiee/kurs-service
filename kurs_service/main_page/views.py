from django.shortcuts import render
from about.models import AboutAdvantages
from main_page.models import (
	MainPageSlider,
	MainPageDirectionOfActivity,
	MainPageAlwaysInStock,
	MainPageAdditionalPowerEquipmentAMTH,
	MainPageAdditionalPowerEquipment,
	MainPageOurAdvantages,
    MainPageOurAdvantagesVideo,
	MainPageQuestions,
	MainPageEverythingToBoBest,
	MainPageProfessionalEquipment,
	MainPageTitles,
)


def main_page(request):
    context = {
        'title': 'Главная страница | OOO "КУРС"',
        'main_page_slider': MainPageSlider.objects.all(),
        'about_advantages': AboutAdvantages.objects.all(),
        'main_page_direction_of_activity': MainPageDirectionOfActivity.objects.all(),
        'main_page_always_in_stock_main_text': MainPageAlwaysInStock.objects.first(),
        'main_page_always_in_stock': MainPageAlwaysInStock.objects.all(),
        'main_page_additional_power_equipment_amth': MainPageAdditionalPowerEquipmentAMTH.objects.first(),
        'main_page_additional_power_equipment': MainPageAdditionalPowerEquipment.objects.all(),
        'main_page_our_advantages': MainPageOurAdvantages.objects.first(),
        'main_page_our_advantages_video': MainPageOurAdvantagesVideo.objects.first(),
        'main_page_questions': MainPageQuestions.objects.all(),
        'main_page_everything_to_be_best_first': MainPageEverythingToBoBest.objects.all()[:4],
        'main_page_everything_to_be_best_last': MainPageEverythingToBoBest.objects.all()[4:],
        'main_page_professional_equipment': MainPageProfessionalEquipment.objects.all(),
        'main_page_titles': MainPageTitles.objects.first(),
    }
    return render(request, "main_page/main_page.html", context=context)
