from django.shortcuts import render
from site_login.models import (
	SiteLoginText,
	SiteLoginTitles,
)


def site_login(request):
    context = {
        'title': 'Вход | OOO "КУРС"',
        'site_login_text': SiteLoginText.objects.first(),
        'site_login_titles': SiteLoginTitles.objects.first(),
    }
    return render(request, "site_login/site_login.html", context=context)
