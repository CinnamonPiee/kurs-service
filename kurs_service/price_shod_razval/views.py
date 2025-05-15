from django.shortcuts import render


def price_shod_razval(request):
	context = {}

	return render(request, 'price_shod_razval/price_shod_razval.html', context)
