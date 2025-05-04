from django.contrib import admin
from .models import (
	ReviewsTitles,
	ReviewsReview,
	ReviewsResponse,
)


@admin.register(ReviewsTitles)
class ReviewsTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(ReviewsReview)
class ReviewsReviewAdmin(admin.ModelAdmin):
	pass


@admin.register(ReviewsResponse)
class ReviewsResponseAdmin(admin.ModelAdmin):
	pass
