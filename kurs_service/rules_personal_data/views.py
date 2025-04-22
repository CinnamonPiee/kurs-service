from django.shortcuts import render
from rules_personal_data.models import (
	RulesPersonalDataObligations,
	RulesPersonalDataMainObligation,
	RulesPersonalDataSliderImages,
	RulesPersonalDataTitles,
)


def rules_personal_data(request):
	context = {
		'title': 'Правила обработки данных | OOO "КУРС"',
		'rules_personal_data_slider_images': RulesPersonalDataSliderImages.objects.first(),
		'rules_personal_data_main_obligation': RulesPersonalDataMainObligation.objects.first(),
		'rules_personal_data_obligations': RulesPersonalDataObligations.objects.all(),
		'rules_personal_data_titles': RulesPersonalDataTitles.objects.first(),
	}
	return render(request, "rules_personal_data/rules_personal_data.html", context=context)
