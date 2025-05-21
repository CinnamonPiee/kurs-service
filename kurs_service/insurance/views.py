from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InsuranceFormModelForm
from .models import (
	InsuranceSliderImages,
	InsuranceBenefitsOfInsuringWithUs,
	InsuranceFrequentlyAskedQuestions,
	InsuranceTitles,
)


def insurance(request):
    if request.method == "POST":
        form = InsuranceFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена! Ожидайте звонка.")
            return redirect("insurance:insurance")
        else:
            messages.error(request, "Ошибка отправки формы. Проверьте введенные данные.")
    else:
        form = InsuranceFormModelForm()
    context = {
        "form": form,
        "title": "Страхование | OOO 'КУРС'",
        "insurance_titles": InsuranceTitles.objects.first(),
        "insurance_slider_images": InsuranceSliderImages.objects.first(),
        "insurance_benefits_of_insuring_with_us": InsuranceBenefitsOfInsuringWithUs.objects.all(),
        "insurance_frequently_asked_questions": InsuranceFrequentlyAskedQuestions.objects.all(),
    }
    return render(request, "insurance/insurance.html", context=context)
