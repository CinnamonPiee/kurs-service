from django.db import models
from django.utils.html import strip_tags


class RulesPersonalDataImages(models.Model):
    img = models.ImageField(upload_to="page_images", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        clean_text = strip_tags(self.description)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "rules_personal_data_images"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Правила обработки данных пользователей"


class RulesPersonalDataObligations(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, 
    verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, 
    verbose_name="Описание")

    def __str__(self):
        clean_text = strip_tags(self.title)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "rules_personal_data_obligations"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Основной текст правил"
        

class RulesPersonalDataTitles(models.Model):
    rules_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст заголовка")
    

    def __str__(self):
        clean_text = strip_tags(self.rules_title)
        return clean_text[:50] if clean_text else "Без названия"

    class Meta:
        db_table = "rules_personal_data_titles"
        verbose_name: str = "заголовок"
        verbose_name_plural: str = "Заголовки"
