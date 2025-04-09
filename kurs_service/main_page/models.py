from django.db import models


class MainPageSlider(models.Model):
	url_slider = models.CharField(max_length=255, null=True, blank=True, verbose_name="Путь к странице")
	img_slider = models.ImageField(upload_to="main_page_slider", null=True, blank=True, verbose_name="Изображение")

	def __str__(self):
		return self.url_slider

	class Meta:
		db_table = "main_page_slider"
		verbose_name: str = "изображение"
		verbose_name_plural: str = "Изображения"


class MainPageDirectionOfActivity(models.Model):
	img = models.ImageField(upload_to="direction_of_activity", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	price = models.IntegerField(default=0, null=True, blank=True, verbose_name="Цена")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "main_page_direction_of_activity"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Основные направления"


class MainPageAlwaysInStock(models.Model):
	main_text = models.TextField(null=True, blank=True, verbose_name="Главное описание")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	img = models.ImageField(upload_to="always_in_stock", null=True, blank=True, verbose_name="Изображение")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "main_page_always_in_stock"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Всегда в наличии"


class MainPageAdditionalPowerEquipmentAMTH(models.Model):
	left_img = models.ImageField(upload_to="additional_power_equipment", null=True, blank=True, verbose_name="Изображение слева")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	right_img = models.ImageField(upload_to="additional_power_equipment", null=True, blank=True, verbose_name="Изображение справа")

	def __str__(self):
		return "О компании АМЗ"

	class Meta:
		db_table = "main_page_additional_power_equipment_amth"
		verbose_name: str = "текст"
		verbose_name_plural: str = "ООО 'КУРС' совместно с компанией АМЗ"


class MainPageAdditionalPowerEquipment(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	img = models.ImageField(upload_to="additional_power_equipment", null=True, blank=True, verbose_name="Изображение")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	button_text = models.CharField(max_length=255, null=True, blank=True, verbose_name="Текст кнопки")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "main_page_additional_power_equipment"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Cиловое дополнительное оборудование"


class MainPageOurAdvantagesVideo(models.Model):
	video = models.CharField(max_length=255, null=True, blank=True, verbose_name="Видео")

	def __str__(self):
		return "Наши преимущества (видео)"

	class Meta:
		db_table = "main_page_our_advantages_video"
		verbose_name: str = "видео"
		verbose_name_plural: str = "Наши преимущества (видео)"


class MainPageOurAdvantages(models.Model):
	text = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		return "Наши преимущества"

	class Meta:
		db_table = "main_page_our_advantages"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Наши преимущества"


class MainPageQuestions(models.Model):
	question = models.TextField(null=True, blank=True, verbose_name="Вопрос")
	answer = models.TextField(null=True, blank=True, verbose_name="Ответ")

	def __str__(self):
		return self.question

	class Meta:
		db_table = "main_page_questions"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Часто задаваемые вопросы"


class MainPageEverythingToBoBest(models.Model):
	img = models.ImageField(upload_to="mini_icons", null=True, blank=True, verbose_name="Изображение")
	title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")

	def __str__(self):
		return self.title

	class Meta:
		db_table = "main_page_everything_to_be_best"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Всё то, чтобы считаться лучшими"


class MainPageProfessionalEquipment(models.Model):
	img = models.ImageField(upload_to="photo_gallery", null=True, blank=True, verbose_name="Изображение")

	def __str__(self):
		return "Изображение"

	class Meta:
		db_table = "main_page_professional_equipment"
		verbose_name: str = "текст"
		verbose_name_plural: str = "Фотографии оборудования"


class MainPageTitles(models.Model):
	direction_of_activity = models.CharField(max_length=255, null=True, blank=True, verbose_name="Направление в деятельности")
	always_in_stock = models.CharField(max_length=255, null=True, blank=True, verbose_name="Всегда в наличии")
	additional_power_equipment = models.CharField(max_length=255, null=True, blank=True, verbose_name="Cиловое дополнительное оборудование")
	our_advantages = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наши преимущества")
	frequently_asked_questions = models.CharField(max_length=255, null=True, blank=True, verbose_name="Часто задаваемые вопросы")
	everything_to_be_best = models.CharField(max_length=255, null=True, blank=True, verbose_name="Всё то, чтобы считаться лучшими")
	professional_equipment = models.CharField(max_length=255, null=True, blank=True, verbose_name="Профессиональное оборудование")

	def __str__(self):
		return "Заголовки"

	class Meta:
		db_table = "main_page_titles"
		verbose_name: str = "заголовки"
		verbose_name_plural: str = "Заголовки"
