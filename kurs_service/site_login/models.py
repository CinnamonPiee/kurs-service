from django.db import models
from django.utils.html import strip_tags


class SiteLoginText(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Пожалуйста, заполните следующие поля для входа")
	mail = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес электронной почты")
	password = models.CharField(max_length=255, null=True, blank=True, verbose_name="Пароль")
	button = models.CharField(max_length=255, null=True, blank=True, verbose_name="Войти")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "site_login_text"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Текст"


class SiteLoginTitles(models.Model):
	enter_forms = models.CharField(max_length=255, null=True, blank=True, verbose_name="Вход")

	def __str__(self):
		clean_text = strip_tags(self.enter_forms)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "site_login_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
