from django.shortcuts import render
from rules_personal_data.models import (
    RulesPersonalDataImages,
	RulesPersonalDataObligations,
	RulesPersonalDataTitles,
)


def rules_personal_data(request):
    context = {
        'title': 'Правила обработки и хранения данных пользователя | OOO "КУРС"',
        'rules_personal_data_images': RulesPersonalDataImages.objects.first(),
        'rules_personal_data_obligations': RulesPersonalDataObligations.objects.all(),
        'rules_personal_data_titles': RulesPersonalDataTitles.objects.first(),
    }
    return render(request, "rules_personal_data/rules_personal_data.html", context=context)
