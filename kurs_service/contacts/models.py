from django.db import models
from django.utils.html import strip_tags


class ContactsImages(models.Model):
	img = models.ImageField(upload_to="page_images", blank=True, null=True, verbose_name="Изображение")
	description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
	mobile_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Номер телефона")

	def __str__(self):
		clean_text = strip_tags(self.description)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "contacts_images"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наши операторы с точностью помогут вам!"


class ContactsWorkingTime(models.Model):
	weekday = models.TextField(blank=True, null=True, 
    verbose_name="День недели")
	weekday_hours = models.TextField(blank=True, null=True, 
    verbose_name="Время работы")

	def __str__(self):
		return self.weekday

	class Meta:
		db_table = "contacts_working_time"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наш режим работы"

	
class ContactsCompanyData(models.Model):
	img_qrcode = models.ImageField(upload_to="qr_codes", blank=True, null=True, verbose_name="QR-код")
	img_qrcode_mobile = models.ImageField(upload_to="qr_codes", blank=True, null=True, verbose_name="Изображение")
	qrcode_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст qr-кода")
	img_email = models.ImageField(upload_to="mini_icons", blank=True, null=True, verbose_name="Изображение почты")
	email_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст почты")
	img_address = models.ImageField(upload_to="mini_icons", blank=True, null=True, verbose_name="Изображение адреса")
	address_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст адреса")
	imp_open = models.ImageField(upload_to="mini_icons", blank=True, null=True, verbose_name="Изображение открыто")
	open_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст открыто")
	imp_watsapp = models.ImageField(upload_to="mini_icons", blank=True, null=True, verbose_name="Изображение WatsApp")
	watsapp_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст WatsApp")
	mobile_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текст мобильного номера")

	def __str__(self):
		return "Наши контактные данные"

	class Meta:
		db_table = "contacts_company_data"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наш контактные данные"

	
class ContactsCompanyDetails(models.Model):
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
		db_table = "contacts_company_details"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Контакты и реквизиты компании ООО 'КУРС'"


class ContactsDirectionSchema(models.Model):
	img_line_metro = models.ImageField(upload_to="directions_schema", blank=True, null=True, verbose_name="Изображение линии метро")
	img_train = models.ImageField(upload_to="directions_schema", blank=True, null=True, verbose_name="Изображение поезда")
	description_train = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на метро")
	img_foot = models.ImageField(upload_to="directions_schema", blank=True, null=True, verbose_name="Изображение пешеходов")
	description_foot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути пешком")
	img_taxi = models.ImageField(upload_to="directions_schema", blank=True, null=True, verbose_name="Изображение такси")
	description_taxi = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание пути на такси")

	def __str__(self):
		return self.description_train

	class Meta:
		db_table = "contacts_direction_schema"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Схема прохода и проезда"

	
class ContactsMapSchema(models.Model):
	img = models.ImageField(upload_to="directions_schema", blank=True, null=True, verbose_name="Изображение")

	def __str__(self):
		return "Изображение карты прохода"

	class Meta:
		db_table = "contacts_map_schema"
		verbose_name: str = "изображение"
		verbose_name_plural: str = "Карта прохода и проезда"


class ContactsTitles(models.Model):
	contacts_and_working_hours = models.CharField(max_length=255, blank=True, null=True, verbose_name="Наши контактные данные и режим работы")
	contacts_and_details = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контакты и реквизиты компании ООО 'КУРС'")
	direction_schema = models.CharField(max_length=255, blank=True, null=True, verbose_name="Схема прохода и проезда")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "contacts_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
