from django.shortcuts import render


def site_login(request):
	context = {
		
	}
	return render(request, "site_login/site_login.html", context=context)