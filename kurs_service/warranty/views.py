from django.shortcuts import render
from warranty.models import WarrantyObligations


def warranty(request):
    context = {
        'title': 'Гарантия | OOO "КУРС"',
        'warranty_text': WarrantyObligations.objects.last(),
    }
    return render(request, "warranty/warranty.html", context=context)
