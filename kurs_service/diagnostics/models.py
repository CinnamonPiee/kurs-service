from django.db import models


class DiagnosticsMainDirections(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
	img = models.ImageField(upload_to="diagnostics_directions", blank=True, null=True, verbose_name="Изображение")
	main_problems = models.CharField(max_length=255, blank=True, null=True, verbose_name="Основные проблемы")
	first_problem = models.CharField(max_length=255, blank=True, null=True, verbose_name="1")
	second_problem = models.CharField(max_length=255, blank=True, null=True, verbose_name="2")
	third_problem = models.CharField(max_length=255, blank=True, null=True, verbose_name="3")
	fourth_problem = models.CharField(max_length=255, blank=True, null=True, verbose_name="4")
	img_fourth_problem = models.ImageField(upload_to="min_icon_warning", blank=True, null=True, verbose_name="Изображение")
	fifth_problem = models.CharField(max_length=255, blank=True, null=True, verbose_name="5")
	button_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Кнопка записи")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "diagnostics_main_directions"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Основные направления диагностики"


class DiagnosticsWikiText(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
	description = models.TextField(blank=True, null=True, verbose_name="Текст")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "diagnostics_wiki_text"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Текст о диагностике"
