from django.shortcuts import render
from .models import (
	DiscountsTitles,
	DiscountsDiscount,
)


def discounts(request):
	context = {
		"title": 'Акции | OOO "КУРС"',
		"discounts_titles": DiscountsTitles.objects.first(),
		"discounts_discount": DiscountsDiscount.objects.all(),
    }

	return render(request, "discounts/discounts.html", context=context)
