from django.shortcuts import render


def price_tire_fitting(request):
	context = {}

	return render(request, 'price_tire_fitting/price_tire_fitting.html', context)
