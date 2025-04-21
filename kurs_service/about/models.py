from django.db import models
from django.utils.html import strip_tags


class AboutLetsAcquainted(models.Model):
	img = models.ImageField(upload_to="img-logo", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_lets_acquainted"
		verbose_name = "текст"
		verbose_name_plural = "Давайте знакомиться"


class AboutOurAdvantages(models.Model):
	advantages_item = models.CharField(max_length=255, null=True, blank=True, verbose_name="Преимущество")

	def __str__(self):
		clean_text = strip_tags(self.advantages_item)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_our_advantages"
		verbose_name = "текст"
		verbose_name_plural = "Наши преимущества"


class AboutBestInBusiness(models.Model):
	img = img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	first_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Первый заголовок")
	second_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Второй заголовок")
	third_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Третий заголовок")

	def __str__(self):
		clean_text = strip_tags(self.first_title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_best_in_business"
		verbose_name = "текст"
		verbose_name_plural = "Лучшие в своем деле"


class AboutContacts(models.Model):
	img = img = models.ImageField(upload_to="site-img", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_contacts"
		verbose_name = "текст"
		verbose_name_plural = "Контакты ООО 'КУРС'"


class AboutAccuratelyInTime(models.Model):
	img = img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	first_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Первый заголовок")
	second_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Второй заголовок")
	third_title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Третий заголовок")

	def __str__(self):
		clean_text = strip_tags(self.first_title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_accurately_in_time"
		verbose_name = "текст"
		verbose_name_plural = "Точно и в срок"


class AboutHowWeTrainingStaff(models.Model):
	img = img = models.ImageField(upload_to="img-staff-training", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "about_how_we_training_staff"
		verbose_name = "текст"
		verbose_name_plural = "Как мы обучаем наш персонал?"


# TODO Доделать модель отзыва после создания моделей отзывов


class AboutTitles(models.Model):
	lets_acquainted = models.CharField(max_length=255, blank=True, null=True, verbose_name="Давайте знакомиться")
	our_advantages = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наши преимущества")
	best_in_business = models.CharField(max_length=255, blank=True, null=True, verbose_name="Лучшие в своем деле")
	contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контакты ООО 'КУРС'")
	accurately_in_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Точно и в срок")
	how_we_training_staff = models.CharField(max_length=255, blank=True, null=True, verbose_name="Как мы обучаем наш персонал?")
	last_review = models.CharField(max_length=255, blank=True, null=True, verbose_name="Последний отзыв о нашей работе")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "about_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
