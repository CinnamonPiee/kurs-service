from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
	OnlineAppointmentSliderImages,
	OnlineAppointmentTitles,
)
from .forms import OnlineAppointmentFormModelForm
from base_page.models import (
	CarBody,
	CarModel, 
	CarModification,
)
from django.http import HttpResponse


def online_appointment(request):
    if request.method == "POST":
        form = OnlineAppointmentFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена! Ожидайте звонка.")
            return redirect("online_appointment:online_appointment")
        else:
            messages.error(request, "Ошибка отправки формы. Проверьте введенные данные.")
    else:
        form = OnlineAppointmentFormModelForm()
    context = {
        'form': form,
        'evacuation_car_type': CarBody.objects.all(),
        'online_appointment_slider_images': OnlineAppointmentSliderImages.objects.first(),
        'online_appointment_title': OnlineAppointmentTitles.objects.first(),
    }
    return render(request, 'online_appointment/online_appointment.html', context)


def get_car_models(request):
    mark_id = request.GET.get('id')
    options = '<option value="">Выберите модель</option>'
    if mark_id:
        models = CarModel.objects.filter(mark_id=mark_id)
        for model in models:
            options += f'<option value="{model.id}">{model.name}</option>'
    return HttpResponse(options)


def get_car_modifications(request):
    model_id = request.GET.get('id')
    options = '<option value="">Выберите модификацию</option>'
    if model_id:
        modifications = CarModification.objects.filter(model_id=model_id)
        for mod in modifications:
            options += f'<option value="{mod.id}">{mod.generation_name}</option>'
    return HttpResponse(options)
