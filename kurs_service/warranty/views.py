from django.shortcuts import render
from warranty.models import (
	WarrantyObligations,
	WarrantyHeaders,
)


def warranty(request):
    context = {
        'title': 'Гарантия | OOO "КУРС"',
        'warranty_text': WarrantyObligations.objects.all(),
        'warranty_headers': WarrantyHeaders.objects.last(),
    }
    return render(request, "warranty/warranty.html", context=context)
