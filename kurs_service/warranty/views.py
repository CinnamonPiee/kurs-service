from django.shortcuts import render
from warranty.models import (
	WarrantySliderImages,
	WarrantyObligations,
	WarrantyTitles,
)


def warranty(request):
	context = {
		'title': 'Гарантия | OOO "КУРС"',
		'warranty_slider_images': WarrantySliderImages.objects.first(),
		'warranty_obligations': WarrantyObligations.objects.all(),
		'warranty_titles': WarrantyTitles.objects.first(),
	}
	return render(request, "warranty/warranty.html", context=context)
