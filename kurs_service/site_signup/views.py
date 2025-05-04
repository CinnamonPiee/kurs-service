from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SiteVisitorSignupForm
from .models import SiteSignupTitles


def site_signup(request):
    if request.method == "POST":
        form = SiteVisitorSignupForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.set_password(form.cleaned_data["password"])
            visitor.save()
            request.session["visitor_email"] = visitor.email
            request.session["visitor_name"] = visitor.first_name
            messages.success(request, f"Регистрация прошла успешно! Добро пожаловать, {visitor.email}!")
            return redirect("main_page:main_page")
        else:
            messages.error(request, "Ошибка регистрации. Проверьте введенные данные.")
    else:
        form = SiteVisitorSignupForm()

    context = {
        "form": form,
        "title": 'Регистрация | OOO "КУРС"',
        'site_signup_titles': SiteSignupTitles.objects.first(),
    }

    return render(request, "site_signup/site_signup.html", context=context)