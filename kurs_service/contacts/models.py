from django.db import models


class SupportHelp(models.Model):
	img = models.ImageField(upload_to="big_png_with_text", blank=True, null=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
	mobile_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

	def __str__(self):
		return "Текст на странице - Гарантии - наши операторы с точностью помогут вам!"

	class Meta:
		db_table = "support_help_title"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наши операторы с точностью помогут вам!"


class WorkingTime(models.Model):
	weekdays = models.TextField(blank=True, null=True, 
    verbose_name="День недели")
	weekdays_hours = models.TextField(blank=True, null=True, 
    verbose_name="Время работы")

	def __str__(self):
		return self.weekdays

	class Meta:
		db_table = "working_time"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наши контактные данные и режим работы"

	
class ContactsData(models.Model):
	img = models.ImageField(upload_to="qr_codes", blank=True, null=True, verbose_name="QR-код")
	second_img = models.ImageField(upload_to="qr_codes", blank=True, null=True, verbose_name="Изображение")
	text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст")
	second_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Второй текст")

	def __str__(self):
		return self.text

	class Meta:
		db_table = "contacts_data"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наши контактные данные и режим работы"

	
class ContactsAndDetails(models.Model):
	mobile_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Номер телефона")
	actual_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фактический адрес")
	legal_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Юридический адрес")
	i_n_n = models.CharField(max_length=255, blank=True, null=True, verbose_name="ИНН")
	k_p_p = models.CharField(max_length=255, blank=True, null=True, verbose_name="КПП")
	r_s = models.CharField(max_length=255, blank=True, null=True, verbose_name="р/с")
	k_s = models.CharField(max_length=255, blank=True, null=True, verbose_name="к/с")
	bik = models.CharField(max_length=255, blank=True, null=True, verbose_name="БИК")

	def __str__(self):
		return "Реквизиты"

	class Meta:
		db_table = "contacts_and_details"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Контакты и реквизиты компании ООО 'КУРС'"


class DirectionScheme(models.Model):
	img_line_metro = models.ImageField(upload_to="directions_to_service", blank=True, null=True, verbose_name="Изображение линии метро")
	img_train = models.ImageField(upload_to="directions_to_service", blank=True, null=True, verbose_name="Изображение поезда")
	description_train = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на метро")
	img_foot = models.ImageField(upload_to="directions_to_service", blank=True, null=True, verbose_name="Изображение пешеходов")
	description_foot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути пешком")
	img_taxi = models.ImageField(upload_to="directions_to_service", blank=True, null=True, verbose_name="Изображение такси")
	description_taxi = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на такси")

	def __str__(self):
		return "Схема"

	class Meta:
		db_table = "direction_scheme"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Схема прохода и проезда"


class ContactsHeaders(models.Model):
	contacts_and_working_hours = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на такси")
	contacts_and_details = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на такси")
	direction_scheme = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на такси")

	def __str__(self):
		return "Текст"

	class Meta:
		db_table = "contacts_headers"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"

