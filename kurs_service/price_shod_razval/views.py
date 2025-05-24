from django.shortcuts import render
from .models import (
	PriceShodRazvalCategory,
	PriceShodRazvalPrice,
)
from discounts.models import DiscountsDiscount
from django.core.paginator import Paginator


def price_shod_razval(request, category_slug=None):
	if category_slug:
		category = PriceShodRazvalCategory.objects.filter(
			slug=category_slug
		).first()
		price_list = PriceShodRazvalPrice.objects.filter(category=category)
	else:
		category = None
		price_list = PriceShodRazvalPrice.objects.all()

	paginator = Paginator(price_list, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	show_pagination = paginator.count > 6

	context = {
		'page_obj': page_obj,
		'show_pagination': show_pagination,
		'category': category,
		'price_shod_razval_categories': PriceShodRazvalCategory.objects.all(),
		'discounts_discount': DiscountsDiscount.objects.first(),
	}

	return render(request, 'price_maintenance/price_maintenance.html', context)
