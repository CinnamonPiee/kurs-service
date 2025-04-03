from django.db import models


class PersonalDataTitle(models.Model):
    img = models.ImageField(upload_to="big_png_with_text", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")

    def __str__(self):
        return "Текст на странице - Правила обработки и хранения данных пользователя - правила обработки данных пользователя"

    class Meta:
        db_table = "personal_data_title"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Правила обработки данных пользователя"


class PersonalDataText(models.Model):
    bold_head = models.TextField(blank=True, null=True, 
    verbose_name="Жирный заголовок")
    description = models.TextField(blank=True, null=True, 
    verbose_name="Пункты")

    def __str__(self):
        return self.bold_head

    class Meta:
        db_table = "personal_data_text"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Правила обработки"
        

class PersonalDataHeaders(models.Model):
    rules = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок1")
    

    def __str__(self):
        return "Текст"

    class Meta:
        db_table = "personal_data_headers"
        verbose_name: str = "заголовок"
        verbose_name_plural: str = "Заголовки"
