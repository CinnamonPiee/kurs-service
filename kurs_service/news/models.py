from django.db import models


class NewsContent(models.Model):
	news_img = models.ImageField(upload_to="news_photo", blank=True, null=True, verbose_name="Изображение с текстом новости")
	img = models.ImageField(upload_to="news_photo", blank=True, null=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
	description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
	posted = models.CharField(max_length=255, blank=True, null=True, verbose_name="Размещение")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "news_content"
		verbose_name: str = "новость"
		verbose_name_plural: str = "Новости"
		