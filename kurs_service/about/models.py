from tabnanny import verbose
from django.db import models


class DescriptionCompany(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Короткое описание")

    def __str__(self):
        return "Текст на странице - О сервисе"

    class Meta:
        db_table = "description_company"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Текст"
        

class Training(models.Model):
    img = models.ImageField(upload_to="staff_training", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "training"
        verbose_name: str = "изображение"
        verbose_name_plural: str = "Изображения"
