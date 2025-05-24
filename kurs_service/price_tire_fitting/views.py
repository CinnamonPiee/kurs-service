from django.shortcuts import render
from .models import (
	PriceTireFittingCategory,
	PriceTireFittingPrice,
)
from discounts.models import DiscountsDiscount
from django.core.paginator import Paginator


def price_tire_fitting(request, category_slug=None):
	if category_slug:
		category = PriceTireFittingCategory.objects.filter(
			slug=category_slug
		).first()
		price_list = PriceTireFittingPrice.objects.filter(category=category)
	else:
		category = None
		price_list = PriceTireFittingPrice.objects.all()

	paginator = Paginator(price_list, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	show_pagination = paginator.count > 6

	context = {
		'page_obj': page_obj,
		'show_pagination': show_pagination,
		'category': category,
		'price_tire_fitting_categories': PriceTireFittingCategory.objects.all(),
		'discounts_discount': DiscountsDiscount.objects.first(),
	}

	return render(request, 'price_tire_fitting/price_tire_fitting.html', context)
