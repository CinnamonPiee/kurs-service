from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import CheckListOrderForm
from .utils import (
    add_to_cart,
    increment_cart_item,
    decrement_cart_item,
    remove_cart_item,
    get_cart_items,
    get_cart_count,
)
from .models import CheckListOrder


def get_user_cart_items(request):
    if request.user.is_authenticated:
        order = (
            CheckListOrder.objects.filter(email=request.user.email, quantity__gt=0)
            .order_by("-created_at")
            .first()
        )
        if order:
            items = [
                {
                    "service_id": item.service_id,
                    "service_name": item.service_name,
                    "img_url": "",
                    "quantity": item.quantity,
                }
                for item in order.items.all()
            ]
            count = sum(item["quantity"] for item in items)
            return items, count
        return [], 0
    else:
        items = get_cart_items(request)
        count = get_cart_count(request)
        return items, count


def check_list(request):
    if request.method == 'POST':
        form = CheckListOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            check_list_items, _ = get_user_cart_items(request)
            
            if request.user.is_authenticated:
                order.email = request.user.email
            
            order.save()

            for item in check_list_items:
                order.items.create(
                    service_id=item['service_id'],
                    service_name=item['service_name'],
                    quantity=item['quantity']
                )
            
            if request.user.is_authenticated:
                CheckListOrder.objects.filter(
                    email=request.user.email,
                    quantity__gt=0
                ).update(quantity=0)
            else:
                request.session['check_list'] = {}
                request.session.modified = True
                
            messages.success(request, 'Заказ успешно оформлен')
            return redirect('check_list:check_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
            
    form = CheckListOrderForm()
    check_list_items, check_list_count = get_user_cart_items(request)
    return render(
        request,
        "check_list/check_list.html",
        {
            "form": form,
            "check_list_items": check_list_items,
            "check_list_count": check_list_count,
        },
    )


def check_list_index(request):
    check_list_items, check_list_count = get_user_cart_items(request)
    return render(
        request,
        "check_list/check_list.html",
        {
            "check_list_items": check_list_items,
            "check_list_count": check_list_count,
            "form": CheckListOrderForm(),
        },
    )


@require_POST
@csrf_exempt
def add_to_check_list(request):
    service_id = request.POST.get("id")
    service_name = request.POST.get("name", "")
    img_url = request.POST.get("img_url", "")
    if not service_id:
        return JsonResponse({"code": 400, "html": "Ошибка: не передан id услуги"})
    add_to_cart(request, service_id, service_name, img_url)
    return JsonResponse({"code": 200, "html": "Услуга добавлена"})


@require_POST
@csrf_exempt
def increment_check_list(request):
    service_id = request.POST.get("id")
    print(f"Received decrement request for service_id: {service_id}")  # Отладочная информация
    if not service_id:
        return JsonResponse({"code": 400, "html": "Ошибка: не передан id услуги"})
    increment_cart_item(request, service_id)
    return JsonResponse({"code": 200, "html": "Количество увеличено"})


@require_POST
@csrf_exempt
def decrement_check_list(request):
    service_id = request.POST.get("id")
    print(f"Received decrement request for service_id: {service_id}")  # Отладочная информация
    if not service_id:
        return JsonResponse({"code": 400, "html": "Ошибка: не передан id услуги"})
    decrement_cart_item(request, service_id)
    return JsonResponse({"code": 200, "html": "Количество уменьшено"})


@require_POST
@csrf_exempt
def remove_check_list_item(request):
    service_id = request.POST.get("id")
    print(f"Received decrement request for service_id: {service_id}")  # Отладочная информация
    if not service_id:
        return JsonResponse({"code": 400, "html": "Ошибка: не передан id услуги"})
    remove_cart_item(request, service_id)
    return JsonResponse({"code": 200, "html": "Услуга удалена"})


def check_list_count(request):
    _, count = get_user_cart_items(request)
    return JsonResponse({"count": count})
