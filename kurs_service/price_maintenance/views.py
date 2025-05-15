from django.shortcuts import render


def price_maintenance(request):
	context = {}

	return render(request, 'price_maintenance/price_maintenance.html', context)