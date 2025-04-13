from django.db import models
from django.utils.html import strip_tags


class PhotoGalleryImages(models.Model):
	img = models.ImageField(upload_to="img-photo-gallery", blank=True, null=True, verbose_name="Изображение")
	description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.description)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "photo_gallery_images"
		verbose_name: str = "фото"
		verbose_name_plural: str = "Фотографии"
		

class PhotoGalleryTitles(models.Model):
	photo_gallery = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст заголовка")

	def __str__(self):
		clean_text = strip_tags(self.photo_gallery)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "photo_gallery_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
