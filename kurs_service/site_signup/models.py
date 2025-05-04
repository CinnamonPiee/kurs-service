from django.db import models
from django.utils.html import strip_tags


class SiteSignupTitles(models.Model):
	signup = models.CharField(max_length=255, blank=True, null=True, verbose_name="Регистрация")

	def __str__(self):
		clean_text = strip_tags(self.signup)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "site_signup_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
