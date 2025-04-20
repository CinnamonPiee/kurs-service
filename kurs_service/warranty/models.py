from django.db import models
from django.utils.html import strip_tags


class WarrantySliderImages(models.Model):
	img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	text = models.TextField(null=True, blank=True, verbose_name="Текст")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "warranty_slider_images"
		verbose_name = "текст"
		verbose_name_plural = "Изображения с текстом"


class WarrantyObligations(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "warranty_obligations"
		verbose_name = "текст"
		verbose_name_plural = "Гарантии"


class WarrantyTitles(models.Model):
	warranty = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст заголовка")

	def __str__(self):
		clean_text = strip_tags(self.warranty)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "warranty_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
