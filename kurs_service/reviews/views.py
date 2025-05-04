from django.shortcuts import render, redirect
from django.contrib import messages
from base_page.models import SiteVisitor
from .models import (
	ReviewsTitles,
)
from .forms import ReviewForm
from .models import ReviewsReview


def reviews(request):
	if request.method == "POST":
		form = ReviewForm(request.POST, request.FILES)
		if form.is_valid():
			review = form.save(commit=False)
			review.user = SiteVisitor.objects.get(email=request.session["visitor_email"])
			review.save()
			messages.success(request, "Ваш отзыв успешно отправлен!")
			return redirect("reviews:reviews")
		else:
			messages.error(request, "Ошибка отправки отзыва. Проверьте введенные данные.")
	else:
		form = ReviewForm()

	context = {
		"reviews": ReviewsReview.objects.filter(has_response=True).select_related("response"),
		"form": form,
		"title": 'Отзывы | OOO "КУРС"',
		"reviews_titles": ReviewsTitles.objects.first(),
	}
	return render(request, "reviews/reviews.html", context=context)

