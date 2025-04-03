from django.shortcuts import render
from rules_personal_data.models import (
    PersonalDataHeaders,
    PersonalDataText,
    PersonalDataTitle,
)


def rules_personal_data(request):
    context = {
        'title': 'Правила обработки и хранения данных пользователя | OOO "КУРС"',
        'personal_title': PersonalDataTitle.objects.last(),
        'personal_text': PersonalDataText.objects.all(),
        'personal_header': PersonalDataHeaders.objects.last(),
    }
    return render(request, "rules_personal_data/rules_personal_data.html", context=context)
