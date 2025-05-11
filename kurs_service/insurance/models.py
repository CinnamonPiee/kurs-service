from django.db import models
from django.utils.html import strip_tags


class InsuranceSliderImages(models.Model):
	img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	text = models.TextField(null=True, blank=True, verbose_name="Текст")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:40] if clean_text else "Без названия"

	class Meta:
		db_table = "insurance_slider_images"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Изображения с текстом"

	
class InsuranceForm(models.Model):
	surname = models.CharField(max_length=255, verbose_name="Фамилия")
	name = models.CharField(max_length=255, verbose_name="Имя")
	patronymic = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
	birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
	driving_experience = models.PositiveIntegerField(default=0, verbose_name="Стаж вождения (лет)")
	vin = models.CharField(max_length=17, verbose_name="VIN")
	car_make = models.CharField(max_length=255, verbose_name="Марка автомобиля")
	car_model = models.CharField(max_length=255, verbose_name="Модель автомобиля")
	engine_power = models.PositiveIntegerField(verbose_name="Мощность двигателя (л.с.)")
	phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
	email = models.EmailField(verbose_name="Электронная почта")
	date_time = models.DateTimeField(verbose_name="Дата и время")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

	def __str__(self):
		return f"{self.surname} {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

	class Meta:
		db_table = "insurance_form"
		verbose_name = "Форма страхования"
		verbose_name_plural = "Заявки на страхование"


class InsuranceBenefitsOfInsuringWithUs(models.Model):
	img = models.ImageField(upload_to="img-insurance", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "insurance_benefits_of_insuring_with_us"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Преимущества страхования у нас"


class InsuranceFrequentlyAskedQuestions(models.Model):
	question = models.CharField(max_length=255, blank=True, null=True, verbose_name="Вопрос")
	answer = models.TextField(blank=True, null=True, verbose_name="Ответ")

	def __str__(self):
		clean_text = strip_tags(self.question)
		return clean_text[:50] if clean_text else "Без названия"

	class Meta:
		db_table = "insurance_frequently_asked_questions"
		verbose_name: str = "вопрос"
		verbose_name_plural: str = "Часто задаваемые вопросы"


class InsuranceTitles(models.Model):
	form = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заполнение формы")
	benefits_of_insuring_with_us = models.CharField(max_length=255, blank=True, null=True, verbose_name="Преимущества страхования у нас")
	frequently_asked_questions = models.CharField(max_length=255, blank=True, null=True, verbose_name="Часто задаваемые вопросы")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "insurance_titles"
		verbose_name: str = "заголовок"
		verbose_name_plural: str = "Заголовки"
