from django.shortcuts import render
from django.http import HttpResponse
from .models import BasePageAddOrderServiceModal


def add_order_service_modal(request):
    service_type = request.GET.get('type')
    modals = list(BasePageAddOrderServiceModal.objects.all())
    modal_obj = None

    if service_type == 't_o' and len(modals) > 0:
        modal_obj = modals[0]
    elif service_type == 'diagnostics' and len(modals) > 1:
        modal_obj = modals[1]
    elif service_type == 'tyre' and len(modals) > 2:
        modal_obj = modals[2]
    elif service_type == 'shod_razval' and len(modals) > 3:
        modal_obj = modals[3]

    if not modal_obj:
        from django.http import Http404
        raise Http404("Модальное окно не найдено")

    context = {'base_page_add_order_service_modal': modal_obj}
    return render(request, 'base_page/modales/add_to_order_services.html', context)
