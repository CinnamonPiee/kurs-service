from django.shortcuts import render
from .models import (
	News,
)


def news(request):
	context = {
		"title": 'Новости | OOO "КУРС"',
		"news": News.objects.all().order_by("-created_at"),
	}
	return render(request, "news/news.html", context=context)