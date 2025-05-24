from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import CheckListOrderForm


def check_list_view(request):
    if request.method == "POST":
        form = CheckListOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, "Ваша заявка успешно отправлена! Ожидайте звонка.")
            return redirect("main_page:main_page")
            # Здесь нужно обработать добавление CheckListOrderItem из POST-данных (например, из скрытых полей или JS)
            # Пример:
            # items = request.POST.getlist('services')  # services - список id услуг
            # for service_id in items:
            #     CheckListOrderItem.objects.create(order=order, service_id=service_id, ...)
            return redirect("check_list_success")
    else:
        form = CheckListOrderForm()
    return render(request, "check_list/check_list.html", {"form": form})


def check_list_count(request):
    count = 0
    return JsonResponse({'count': count})
