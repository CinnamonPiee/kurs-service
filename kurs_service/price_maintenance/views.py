from django.shortcuts import render
from .models import (
	PriceMaintenanceCategory,
	PriceMaintenancePrice
)
from discounts.models import DiscountsDiscount
from django.core.paginator import Paginator


def price_maintenance(request):
	price_list = PriceMaintenancePrice.objects.all()
	paginator = Paginator(price_list, 6)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	show_pagination = paginator.count > 6

	context = {
		'page_obj': page_obj,
		'show_pagination': show_pagination,
		'price_maintenance_zamena_masla': PriceMaintenanceCategory.objects.filter(parent_id=1),
		'price_maintenance_zamena_svechey': PriceMaintenanceCategory.objects.filter(parent_id=2),
		'price_maintenance_zamena_filtrov': PriceMaintenanceCategory.objects.filter(parent_id=3),
		'price_maintenance_tormoznaya_sistema': PriceMaintenanceCategory.objects.filter(parent_id=4),
		'price_maintenance_sistema_ohlazhdeniya_otopleniya': PriceMaintenanceCategory.objects.filter(parent_id=5),
		'discounts_discount': DiscountsDiscount.objects.first(),
	}

	return render(request, 'price_maintenance/price_maintenance.html', context)