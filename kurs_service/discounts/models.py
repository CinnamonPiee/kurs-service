from django.db import models
from django.utils.html import strip_tags


class DiscountsDiscount(models.Model):
	little_img = models.ImageField(upload_to="site-img", null=True, blank=True, verbose_name="Маленькое изображение")
	large_img = models.ImageField(upload_to="img-discounts", null=True, blank=True, verbose_name="Большое изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "discounts_discount"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Акции"


class DiscountsTitles(models.Model):
	discounts = models.CharField(max_length=255, blank=True, null=True, verbose_name="Акции")

	def __str__(self):
		clean_text = strip_tags(self.discounts)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "discounts_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
