from django.db import models
from django.utils.html import strip_tags


class WarrantyImages(models.Model):
    img = models.ImageField(upload_to="page_images", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        clean_text = strip_tags(self.description)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "warranty_images"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Гарантия до 180 дней"


class WarrantyObligations(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, 
    verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, 
    verbose_name="Описание")

    def __str__(self):
        clean_text = strip_tags(self.title)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "warranty_obligations"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Основной текст гарантий"
        

class WarrantyTitles(models.Model):
    warranty_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст заголовка")

    def __str__(self):
        clean_text = strip_tags(self.warranty_title)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "warranty_titles"
        verbose_name: str = "заголовок"
        verbose_name_plural: str = "Заголовки"
