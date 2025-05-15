from django.db import models
from django.utils.html import strip_tags


class EvacuationSliderImages(models.Model):
	img = models.ImageField(upload_to='img-slider', blank=True, null=True, verbose_name='Изображение')
	text = models.TextField(blank=True, null=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'evacuation_slider_images'
		verbose_name = 'текст'
		verbose_name_plural = 'Изображения слайдера эвакуации'


class EvacuationForm(models.Model):
    name_user = models.CharField(max_length=255, verbose_name="Имя пользователя")
    call_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    data_time_order = models.DateTimeField(verbose_name="Дата и время заказа")
    car_body = models.CharField(max_length=255, verbose_name="Кузов автомобиля")
    comment_user = models.TextField(blank=True, null=True, verbose_name="Комментарий пользователя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        db_table = "evacuation_form"
        verbose_name = "Заявка на эвакуацию"
        verbose_name_plural = "Заявки на эвакуацию"


class EvacuationFree(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		return self.title
	
	class Meta:
		db_table = 'evacuation_free'
		verbose_name = 'Эвакуация'
		verbose_name_plural = 'Ознакомьтесь с дополнительной информацией'


class EvacuationPricesInCaseOfRefusalToRepairThead(models.Model):
	number = models.CharField(max_length=255, verbose_name='Номер')
	vehicle_category = models.CharField(max_length=255, verbose_name='Категория ТС')
	weight_category = models.CharField(max_length=255, verbose_name='Категория веса')
	price_for_evacuation = models.CharField(max_length=255, verbose_name='Цена эвакуации')

	def __str__(self):
		return self.vehicle_category
	
	class Meta:
		db_table = 'evacuation_prices_in_case_of_refusal_to_repair_thead'
		verbose_name = 'текст'
		verbose_name_plural = 'Цены на эвакуацию в случае отказа от ремонта - заголовок'


class EvacuationPricesInCaseOfRefusalToRepairTbody(models.Model):
	vehicle_category = models.CharField(max_length=255, verbose_name='Категория ТС')
	weight_category = models.CharField(max_length=255, verbose_name='Категория веса')
	price_for_evacuation = models.CharField(max_length=255, verbose_name='Цена эвакуации')

	def __str__(self):
		return self.vehicle_category
	
	class Meta:
		db_table = 'evacuation_prices_in_case_of_refusal_to_repair_tbody'
		verbose_name = 'текст'
		verbose_name_plural = 'Цены на эвакуацию в случае отказа от ремонта - тело'


class EvacuationPricesForAdditionalEvacuationServicesThead(models.Model):
	number = models.CharField(max_length=255, verbose_name='Номер')
	additional_service_category = models.CharField(max_length=255, verbose_name='Категория дополнительной услуги')
	additional_service_price = models.CharField(max_length=255, verbose_name='Цена дополнительной услуги')

	def __str__(self):
		return self.additional_service_category
	
	class Meta:
		db_table = 'evacuation_prices_for_additional_evacuation_services_thead'
		verbose_name = 'текст'
		verbose_name_plural = 'Цены на дополнительные услуги эвакуации - заголовок'


class EvacuationPricesForAdditionalEvacuationServicesTbody(models.Model):
	additional_service_category = models.CharField(max_length=255, verbose_name='Категория дополнительной услуги')
	additional_service_price = models.CharField(max_length=255, verbose_name='Цена дополнительной услуги')

	def __str__(self):
		return self.additional_service_category
	
	class Meta:
		db_table = 'evacuation_prices_for_additional_evacuation_services_tbody'
		verbose_name = 'текст'
		verbose_name_plural = 'Цены на дополнительные услуги эвакуации - тело'


class EvacuationTitles(models.Model):
	fill_out_the_form = models.CharField(max_length=255, verbose_name='Заполните форму')
	read_more_information = models.CharField(max_length=255, verbose_name='Ознакомтесь с дополнительной информацией')

	def __str__(self):
		return "Заголовки"
	
	class Meta:
		db_table = 'evacuation_titles'
		verbose_name = 'Заголовки'
		verbose_name_plural = 'Заголовки'

	
