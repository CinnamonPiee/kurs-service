from django.shortcuts import render


def rules_personal_data(request):
    context = {
        'title': 'Правила обработки и хранения данных пользователя | OOO "КУРС"',
    }
    return render(request, "rules_personal_data/rules_personal_data.html", context=context)
