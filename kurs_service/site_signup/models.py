from django.db import models
from django.utils.html import strip_tags


class SiteSignupText(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Пожалуйста, заполните следующие поля, чтобы зарегистрироваться")
	name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ваше имя")
	mail = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес электронной почты")
	password = models.CharField(max_length=255, null=True, blank=True, verbose_name="Пароль")
	password_repeat = models.CharField(max_length=255, null=True, blank=True, verbose_name="Повторите пароль")
	button = models.CharField(max_length=255, null=True, blank=True, verbose_name="Зарегистрироваться")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "site_signup_text"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Текст"


class SiteSignupTitles(models.Model):
	registration = models.CharField(max_length=255, null=True, blank=True, verbose_name="Регистрация")

	def __str__(self):
		clean_text = strip_tags(self.registration)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "site_signup_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
