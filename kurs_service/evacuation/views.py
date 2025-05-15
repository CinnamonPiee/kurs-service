from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EvacuationFormModelForm
from .models import (
    EvacuationSliderImages,
    EvacuationFree,
    EvacuationPricesInCaseOfRefusalToRepairThead,
    EvacuationPricesInCaseOfRefusalToRepairTbody,
    EvacuationPricesForAdditionalEvacuationServicesThead,
    EvacuationPricesForAdditionalEvacuationServicesTbody,
    EvacuationTitles,
)
from base_page.models import CarBody


def evacuation(request):
    if request.method == "POST":
        form = EvacuationFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена! Ожидайте звонка.")
            return redirect("evacuation:evacuation")
        else:
            messages.error(request, "Ошибка отправки формы. Проверьте введенные данные.")
    else:
        form = EvacuationFormModelForm()

    context = {
        'form': form,
        'evacuation_slider_images': EvacuationSliderImages.objects.first(),
        'evacuation_car_type': CarBody.objects.all(),
        'evacuation_free': EvacuationFree.objects.first(),
        'evacuation_prices_in_case_of_refusal_to_repair_thead': EvacuationPricesInCaseOfRefusalToRepairThead.objects.first(),
        'evacuation_prices_in_case_of_refusal_to_repair_tbody': EvacuationPricesInCaseOfRefusalToRepairTbody.objects.all()[:5],
        'evacuation_prices_in_case_of_refusal_to_repair_tbody_last_two_first': EvacuationPricesInCaseOfRefusalToRepairTbody.objects.all()[5:][0],
        'evacuation_prices_in_case_of_refusal_to_repair_tbody_last_two_second': EvacuationPricesInCaseOfRefusalToRepairTbody.objects.all()[5:][1],
        'evacuation_prices_for_additional_evacuation_services_thead': EvacuationPricesForAdditionalEvacuationServicesThead.objects.first(),
        'evacuation_prices_for_additional_evacuation_services_tbody': EvacuationPricesForAdditionalEvacuationServicesTbody.objects.all(),
        'evacuation_titles': EvacuationTitles.objects.first(),
    }
    
    return render(request, 'evacuation/evacuation.html', context)
