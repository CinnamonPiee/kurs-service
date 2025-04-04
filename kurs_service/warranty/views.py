from django.shortcuts import render
from warranty.models import (
    WarrantyImages,
	WarrantyObligations,
	WarrantyTitles,
)


def warranty(request):
    context = {
        'title': 'Гарантия | OOO "КУРС"',
        'warranty_images': WarrantyImages.objects.first(),
        'warranty_obligations': WarrantyObligations.objects.all(),
        'warranty_titles': WarrantyTitles.objects.first(),
    }
    return render(request, "warranty/warranty.html", context=context)
