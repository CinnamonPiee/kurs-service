from django.db import models


class AboutImages(models.Model):
    img = models.ImageField(upload_to="page_images", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    first_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 1")
    second_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание 2")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "about_images"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Изображения с текстом"


class AboutDescriptionCompany(models.Model):
    img = models.ImageField(upload_to="kurs_logo", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Короткое описание")

    def __str__(self):
        return "Давайте знакомиться"

    class Meta:
        db_table = "about_description_company"
        verbose_name: str = "описание"
        verbose_name_plural: str = "Давайте знакомиться"


class AboutAdvantages(models.Model):
    num_big_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Число")
    big_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")
    num_small_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Число")
    small_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")   

    def __str__(self):
        return f"{self.num_big_text} {self.big_text} {self.num_small_text} {self.small_text} {self.description}"

    class Meta:
        db_table = "about_advantages"
        verbose_name: str = "текст"
        verbose_name_plural: str = "Наши преимущества"  


class AboutContacts(models.Model):
    img = models.ImageField(upload_to="mini_icons", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "about_contacts"
        verbose_name: str = "контакт"
        verbose_name_plural: str = 'Контакты ООО "КУРС"'


class AboutTrainingStaff(models.Model):
    img = models.ImageField(upload_to="staff_training", blank=True, null=True, verbose_name="Изображение")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "about_training_staff"
        verbose_name: str = "изображение"
        verbose_name_plural: str = "Как мы обучаем наш персонал?"


class AboutTitles(models.Model):
    description_company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Давайте знакомиться")
    advantages = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наши преимущества")
    best_in_business = models.CharField(max_length=255, blank=True, null=True, verbose_name="Лучшие в своем деле")
    contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контакты ООО 'КУРС'")
    accurately_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Точно и в срок")
    training = models.CharField(max_length=255, blank=True, null=True, 
    verbose_name="Как мы обучаем наш персонал?")
    last_review = models.CharField(max_length=255, blank=True, null=True, verbose_name="Последний отзыв о нашей работе")

    def __str__(self):
        return "Заголовки"

    class Meta:
        db_table = "about_titles"
        verbose_name: str = "заголовки"
        verbose_name_plural: str = "Заголовки"
