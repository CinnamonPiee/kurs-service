from django.db import models


class ReviewsTitles(models.Model):
	visitor_reviews = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отзывы посетителей")
	leave_review_or_request = models.CharField(max_length=255, null=True, blank=True, verbose_name="Оставьте отзыв или пожелание")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "reviews_titles"
		verbose_name: str = "заголовки"
		verbose_name_plural: str = "Заголовки"
