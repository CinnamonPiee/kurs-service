from django.db import models
from django.utils.html import strip_tags


class DiagnosticsComputerOfCars(models.Model):
	img = models.ImageField(upload_to='img', null=True, blank=True, verbose_name='Изображение')
	first = models.TextField(null=True, blank=True, verbose_name='Первый текст')
	second = models.TextField(null=True, blank=True, verbose_name='Второй текст')
	third = models.TextField(null=True, blank=True, verbose_name='Третий текст')
	fourth = models.TextField(null=True, blank=True, verbose_name='Четвертый текст')
	fifth = models.TextField(null=True, blank=True, verbose_name='Пятый текст')
	img_icon = models.ImageField(upload_to='img-icons', null=True, blank=True, verbose_name='Изображение иконки')

	def __str__(self):
		return 'Компьютерная диагностика автомобилей'
	
	class Meta:
		db_table = 'diagnostics_computer_of_cars'
		verbose_name = 'текст'
		verbose_name_plural = 'Компьютерная диагностика автомобилей'


class DiagnosticsSuspension(models.Model):
	img = models.ImageField(upload_to='img', null=True, blank=True, verbose_name='Изображение')
	first = models.TextField(null=True, blank=True, verbose_name='Первый текст')
	second = models.TextField(null=True, blank=True, verbose_name='Второй текст')
	third = models.TextField(null=True, blank=True, verbose_name='Третий текст')
	fourth = models.TextField(null=True, blank=True, verbose_name='Четвертый текст')
	fifth = models.TextField(null=True, blank=True, verbose_name='Пятый текст')
	img_icon = models.ImageField(upload_to='img-icons', null=True, blank=True, verbose_name='Изображение иконки')

	def __str__(self):
		return 'Диагностика подвески'
	
	class Meta:
		db_table = 'diagnostics_suspension'
		verbose_name = 'текст'
		verbose_name_plural = 'Диагностика подвески'


class DiagnosticsGearbox(models.Model):
	img = models.ImageField(upload_to='img', null=True, blank=True, verbose_name='Изображение')
	first = models.TextField(null=True, blank=True, verbose_name='Первый текст')
	second = models.TextField(null=True, blank=True, verbose_name='Второй текст')
	third = models.TextField(null=True, blank=True, verbose_name='Третий текст')
	fourth = models.TextField(null=True, blank=True, verbose_name='Четвертый текст')
	fifth = models.TextField(null=True, blank=True, verbose_name='Пятый текст')
	img_icon = models.ImageField(upload_to='img-icons', null=True, blank=True, verbose_name='Изображение иконки')

	def __str__(self):
		return 'Диагностика коробки передач'
	
	class Meta:
		db_table = 'diagnostics_gearbox'
		verbose_name = 'текст'
		verbose_name_plural = 'Диагностика коробки передач'


class DiagnosticsComputerGoals(models.Model):
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'diagnostics_computer_diagnostics_goals'
		verbose_name = 'текст'
		verbose_name_plural = 'Цели и задачи компьютерной диагностики'


class DiagnosticsStager(models.Model):
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'diagnostics_stager'
		verbose_name = 'текст'
		verbose_name_plural = 'Этапы диагностики'


class DiagnosticsWhenToGet(models.Model):
	text = models.TextField(null=True, blank=True, verbose_name='Текст')

	def __str__(self):
		clean_text = strip_tags(self.text)
		return clean_text[:50] if clean_text else "Без названия"
	
	class Meta:
		db_table = 'diagnostics_when_to_get'
		verbose_name = 'текст'
		verbose_name_plural = 'Когда нужно делать диагностику'


class DiagnosticsTitles(models.Model):
	computer_diagnostics_of_cars = models.CharField(max_length=255, null=True, blank=True, verbose_name='Компьютерная диагностика автомобилей')
	suspension_diagnostics = models.CharField(max_length=255, null=True, blank=True, verbose_name='Диагностика подвески')
	gearbox_diagnostics = models.CharField(max_length=255, null=True, blank=True, verbose_name='Диагностика коробки передач')
	computer_diagnostics_goals = models.CharField(max_length=255, null=True, blank=True, verbose_name='Цели и задачи компьютерной диагностики')
	stages_of_diagnostics = models.CharField(max_length=255, null=True, blank=True, verbose_name='Этапы диагностики')
	when_to_get_diagnosed = models.CharField(max_length=255, null=True, blank=True, verbose_name='Когда нужно делать диагностику')

	def __str__(self):
		return 'Заголовки'

	class Meta:
		db_table = 'diagnostics_titles'
		verbose_name = 'Заголовки'
		verbose_name_plural = 'Заголовки'
