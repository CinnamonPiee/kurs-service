from django.shortcuts import render
from discounts.models import (
	DiscountsContent,
	DiscountsTitles,
)


def discounts(request):
    context = {
        'title': 'Акции | OOO "КУРС"',
        'discounts_content': DiscountsContent.objects.all(),
        'discounts_titles': DiscountsTitles.objects.first(),
    }
    return render(request, "discounts/discounts.html", context=context)
