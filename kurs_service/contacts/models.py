from django.db import models
from django.utils.html import strip_tags


class ContactsSliderImages(models.Model):
	img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	text = models.TextField(null=True, blank=True, verbose_name="Текст")
	number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Номер телефона")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:40] if clean_text else "Без названия"
	
	class Meta:
		db_table = "contacts_slider_images"
		verbose_name = "текст"
		verbose_name_plural = "Изображения с текстом"


class ContactsWeekdayWorkingTime(models.Model):
	weekday = models.CharField(max_length=255, blank=True, null=True, verbose_name="День недели")
	time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Рабочее время")

	def __str__(self):
		clean_text = strip_tags(self.weekday)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "contacts_weekday_working_time"
		verbose_name = "текст"
		verbose_name_plural = "Наше время работы"


class ContactsDataContacts(models.Model):
	img = models.ImageField(upload_to="site-img", null=True, blank=True, verbose_name="Изображение")
	second_img = models.ImageField(upload_to="site-img", null=True, blank=True, verbose_name="Изображение")
	text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Данные")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "contacts_data_contacts"
		verbose_name = "текст"
		verbose_name_plural = "Наши контактные данные"


class ContactsDetailsAndContacts(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Реквизит")
	description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "contacts_details_and_contacts"
		verbose_name = "текст"
		verbose_name_plural = "Контакты и реквизиты компании ООО 'КУРС'"


class ContactsSchemeAndDetails(models.Model):
	line_metro_img = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Линия метро")
	img_train = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Изображение поезда")
	text_train = models.CharField(max_length=255, blank=True, null=True, verbose_name="Данные поезда")
	img_foot = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Изображение пешеходов")
	text_foot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Данные пешеходов")
	img_taxi = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Изображение такси")
	text_taxi = models.CharField(max_length=255, blank=True, null=True, verbose_name="Данные такси")

	def __str__(self):
		clean_text = strip_tags(self.text_train)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "contacts_scheme_and_details"
		verbose_name = "текст"
		verbose_name_plural = "Схема прохода и проезда"


class ContactsSchemeImage(models.Model):
	img = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Изображение")
	img_max = models.ImageField(upload_to="way-scheme", null=True, blank=True, verbose_name="Изображение")

	def __str__(self):
		return "Изображение"
	
	class Meta:
		db_table = "contacts_scheme_image"
		verbose_name = "изображение"
		verbose_name_plural = "Изображение схемы прохода и проезда"


class ContactsTitles(models.Model):
	contact_data_and_working_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наши контактные данные и режим работы")
	contacts_and_details = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контакты и реквизиты компании ООО 'КУРС'")
	way_scheme = models.CharField(max_length=255, blank=True, null=True, verbose_name="Схема прохода и проезда")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "contacts_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
