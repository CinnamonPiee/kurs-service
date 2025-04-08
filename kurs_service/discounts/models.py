from django.db import models
from django.utils.html import strip_tags



class DiscountsContent(models.Model):
	img_logo = models.ImageField(upload_to="discounts_images", null=True, blank=True, verbose_name="Изображение сверху")
	img = models.ImageField(upload_to="discounts_images", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	button_text = models.CharField(max_length=255, null=True, blank=True, verbose_name="Текст кнопки")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "discounts_content"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Акции"


class DiscountsTitles(models.Model):
	discount = models.CharField(max_length=255, blank=True, null=True, verbose_name="Акции от ООО 'КУРС'")

	def __str__(self):
		return self.dis

	class Meta:
		db_table = "discounts_titles"
		verbose_name: str = "заголовки"
		verbose_name_plural: str = "Заголовки"
