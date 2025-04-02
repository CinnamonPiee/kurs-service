from django.db import models


class DescriptionCompany(models.Model):
    img = models.ImageField(upload_to="kurs_logo", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Короткое описание")

    def __str__(self):
        return "Текст на странице - О сервисе - давайте знакомиться"

    class Meta:
        db_table = "description_company"
        verbose_name: str = "описание"
        verbose_name_plural: str = "Давайте знакомиться"


class Advantages(models.Model):
    num_big_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Число")
    big_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")
    num_small_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Число")
    small_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")   

    def __str__(self):
        return f"{self.num_big_text} {self.big_text} {self.num_small_text} {self.small_text} {self.description}"

    class Meta:
        db_table = "advantages"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Наши преимущества"  


class BestInBusiness(models.Model):
    img = models.ImageField(upload_to="big_png_with_text", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Кроткое описание")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return "Текст на странице - О сервисе - лучшие в своем деле"

    class Meta:
        db_table = "best_in_business"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Лучшие в своем деле"


class Contacts(models.Model):
    img = models.ImageField(upload_to="mini_icons_on_page", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "contacts"
        verbose_name: str = "контакт"
        verbose_name_plural: str = 'Контакты ООО "КУРС"'


class AccuratelyTime(models.Model):
    img = models.ImageField(upload_to="big_png_with_text", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Кроткое описание")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return "Текст на странице - О сервисе - точно и в срок"

    class Meta:
        db_table = "accurately_time"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Точно и в срок"


class Training(models.Model):
    img = models.ImageField(upload_to="staff_training", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "training"
        verbose_name: str = "изображение"
        verbose_name_plural: str = "Как мы обучаем наш персонал?"


class AboutHeaders(models.Model):
    description_company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок1")
    advantages = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок2")
    best_in_business = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок3")
    contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок4")
    accurately_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок5")
    training = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок6")
    last_review = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок7")

    def __str__(self):
        return "Текст"

    class Meta:
        db_table = "about_headers"
        verbose_name: str = "заголовок"
        verbose_name_plural: str = "Заголовки"
