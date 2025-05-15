from django.db import models
from django.utils.html import strip_tags


class OnlineAppointmentSliderImages(models.Model):
	img = models.ImageField(upload_to="img-slider", null=True, blank=True, verbose_name="Изображение")
	text = models.CharField(max_length=255, null=True, blank=True, verbose_name="Текст на слайде")

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = "online_appointment_slider_images"
		verbose_name = "Изображение слайдера онлайн записи"
		verbose_name_plural = "Изображения слайдера онлайн записи"


class OnlineAppointmentForm(models.Model):
    name_user = models.CharField(max_length=255, verbose_name="Имя пользователя")
    call_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    title_services = models.CharField(max_length=255, verbose_name="Название услуги")
    car_mark = models.CharField(max_length=255, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=255, verbose_name="Модель автомобиля", blank=True, null=True)
    car_modification = models.CharField(max_length=255, verbose_name="Модификация (поколение)", blank=True, null=True)
    car_body = models.CharField(max_length=255, verbose_name="Кузов автомобиля", blank=True, null=True)
    date_time_order = models.DateTimeField(verbose_name="Дата и время заказа")
    comment_user = models.TextField(blank=True, null=True, verbose_name="Комментарий пользователя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name_user} - {self.title_services} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
	
    class Meta:
        db_table = "online_appointment_form"
        verbose_name = "Форма онлайн записи"
        verbose_name_plural = "Формы онлайн записи"


class OnlineAppointmentTitles(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заполните форму и мы свяжемся с вами")

	def __str__(self):
		return self.title if self.title else "Без названия"

	class Meta:
		db_table = "online_appointment_titles"
		verbose_name = "Заголовок онлайн записи"
		verbose_name_plural = "Заголовки онлайн записи"
