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


class MainPageAlwaysInStock(models.Model):
	img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Изображение')
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_always_in_stock'
		verbose_name = 'текст'
		verbose_name_plural = 'Всегда в наличии'


class MainPageAdditionalPowerEquipmentAMZ(models.Model):
	left_img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Изображение')
	right_img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Изображение')
	text = models.TextField(blank=True, null=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_additional_power_equipment_amz'
		verbose_name = 'текст'
		verbose_name_plural = 'Дополнительное оборудование AMZ'


class MainPageAdditionalPowerEquipment(models.Model):
	img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Изображение')
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_additional_power_equipment'
		verbose_name = 'текст'
		verbose_name_plural = 'Дополнительное оборудование'


class MainPageOurAdvantages(models.Model):
	video = models.FileField(upload_to='video', blank=True, null=True, verbose_name='Видео')
	text = models.TextField(blank=True, null=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_our_advantages'
		verbose_name = 'текст'
		verbose_name_plural = 'Наши преимущества'


class MainPageFrequentlyAskedQuestions(models.Model):
	question = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вопрос')
	answer = models.TextField(blank=True, null=True, verbose_name='Ответ')

	def __str__(self):
		clean_text = strip_tags(self.question)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_frequently_asked_questions'
		verbose_name = 'текст'
		verbose_name_plural = 'Часто задаваемые вопросы'


class MainPageEverythingToBeConsideredTheBest(models.Model):
	img = models.ImageField(upload_to='img-icons', blank=True, null=True, verbose_name='Изображение')
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Заголовок')
	description = models.TextField(blank=True, null=True, verbose_name='Описание')

	def __str__(self):
		clean_text = strip_tags(self.title)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'main_page_everything_to_be_considered_the_best'
		verbose_name = 'текст'
		verbose_name_plural = 'Всё, чтобы быть лучшим'


class MainPageProfessionalEquipment(models.Model):
	img = models.ImageField(upload_to='img-photo-gallery', blank=True, null=True, verbose_name='Изображение')

	def __str__(self):
		return "Изображения"
	
	class Meta:
		db_table = 'main_page_professional_equipment'
		verbose_name = 'изображение'
		verbose_name_plural = 'Профессиональное оборудование'

	
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
