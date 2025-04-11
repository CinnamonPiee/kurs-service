from django.shortcuts import render
from site_signup.models import (
	SiteSignupText,
	SiteSignupTitles,
)


def site_signup(request):
    context = {
        'title': 'Регистрация | OOO "КУРС"',
        'site_signup_text': SiteSignupText.objects.first(),
        'site_signup_titles': SiteSignupTitles.objects.first(),
    }
    return render(request, "site_signup/site_signup.html", context=context)
