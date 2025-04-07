from django.contrib import admin
from news.models import NewsContent


@admin.register(NewsContent)
class NewsContentAdmin(admin.ModelAdmin):
	pass
