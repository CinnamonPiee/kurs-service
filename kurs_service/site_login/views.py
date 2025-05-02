from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SiteVisitorLoginForm
from .models import SiteLoginTitles


def site_login(request):
	if request.method == "POST":
		form = SiteVisitorLoginForm(request.POST)
		if form.is_valid():
			visitor = form.cleaned_data["visitor"]
			request.session["visitor_email"] = visitor.email
			messages.success(request, f"Добро пожаловать, {visitor.email}!")
			return redirect("main_page:main_page")
		else:
			messages.error(request, "Ошибка авторизации. Проверьте введенные данные.")
	else:
		form = SiteVisitorLoginForm()

	context = {
        "form": form,
		"title": "Авторизация",
        "site_login_titles": SiteLoginTitles.objects.first(),
    }

	return render(request, "site_login/site_login.html", context=context)


def site_logout(request):
    if "visitor_email" in request.session:
        del request.session["visitor_email"]
    return redirect("main_page:main_page")