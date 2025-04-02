from django.shortcuts import render
from warranty.models import (
	WarrantyObligations,
	WarrantyHeaders,
    Warranty180,
)


def warranty(request):
    context = {
        'title': 'Гарантия | OOO "КУРС"',
        'warranty_text': WarrantyObligations.objects.first(),
        'warranty_headers': WarrantyHeaders.objects.last(),
        'warranty_180': Warranty180.objects.last(),
    }
    return render(request, "warranty/warranty.html", context=context)
