from django.db import models
from django.utils.html import strip_tags


class News(models.Model):
	img = models.ImageField(upload_to="img-news", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "news"
		verbose_name: str = "новость"
		verbose_name_plural: str = "Новости"
