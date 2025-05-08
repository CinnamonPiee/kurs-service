from django.db import models
from django.utils.html import strip_tags


class MainPageSliderImages(models.Model):
	image = models.ImageField(upload_to='img-slider', blank=True, null=True, verbose_name='Изображение')
	link = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ссылка')
	
	def __str__(self):
		return "Изображения слайдера"
	
	class Meta:
		db_table = 'main_page_slider_images'
		verbose_name = 'изображение'
		verbose_name_plural = 'Изображения слайдера главной страницы'


class MainPageDirectionOfActivity(models.Model):
	img = models.ImageField(upload_to='img-direction-activity', blank=True, null=True, verbose_name='Изображение')
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')
	price = models.CharField(max_length=255, blank=True, null=True, verbose_name='Цена')

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_direction_of_activity'
		verbose_name = 'текст'
		verbose_name_plural = 'Направление в деятельности'


class MainPageAdditionalPowerEquipmentAMZ(models.Model):
	pass


class MainPageAdditionalPowerEquipment(models.Model):
	pass

	
class MainPageTitles(models.Model):
	direction_of_activity = models.CharField(max_length=255, blank=True, null=True, verbose_name='Направление деятельности')
	always_in_stock = models.CharField(max_length=255, blank=True, null=True, verbose_name='Всегда в наличии')
	additional_power_equipment = models.CharField(max_length=255, blank=True, null=True, verbose_name='Дополнительное оборудование')
	our_advantages = models.CharField(max_length=255, blank=True, null=True, verbose_name='Наши преимущества')
	frequently_asked_questions = models.CharField(max_length=255, blank=True, null=True, verbose_name='Часто задаваемые вопросы')
	everything_to_be_considered_the_best = models.CharField(max_length=255, blank=True, null=True, verbose_name='Всё, чтобы быть лучшим')
	professional_equipment = models.CharField(max_length=255, blank=True, null=True, verbose_name='Профессиональное оборудование')

	def __str__(self):
		return "Заголовки"
	
	class Meta:
		db_table = 'main_page_titles'
		verbose_name = 'заголовок'
		verbose_name_plural = 'Заголовки'
