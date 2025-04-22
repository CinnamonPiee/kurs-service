from django.db import models
from django.utils.html import strip_tags


class RulesPersonalDataSliderImages(models.Model):
	img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	text = models.TextField(null=True, blank=True, verbose_name="Текст")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "rules_personal_data_slider_images"
		verbose_name = "текст"
		verbose_name_plural = "Изображения с текстом"


class RulesPersonalDataMainObligation(models.Model):
	main_description = models.TextField(null=True, blank=True, verbose_name="Описание правил")

	def __str__(self):
		clean_text = strip_tags(self.main_description)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "rules_personal_data_main_obligation"
		verbose_name = "текст"
		verbose_name_plural = "Главное правило"


class RulesPersonalDataObligations(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "rules_personal_data_obligations"
		verbose_name = "текст"
		verbose_name_plural = "Основные правила"


class RulesPersonalDataTitles(models.Model):
	rules_personal_data = models.CharField(max_length=255, blank=True, null=True, verbose_name="Правила обработки данных")

	def __str__(self):
		clean_text = strip_tags(self.rules_personal_data)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "rules_personal_data_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
