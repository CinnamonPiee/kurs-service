from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class SiteVisitor(models.Model):
    img = models.ImageField(default="img-reviews/noavatar_man.png", null=True, blank=True, verbose_name="Изображение")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=15, verbose_name="Телефон", blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name="Пароль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Последний вход")
    is_frequent = models.BooleanField(default=False, verbose_name="Частый клиент")
    visit_count = models.PositiveIntegerField(default=0, verbose_name="Количество посещений")
    notes = models.TextField(blank=True, null=True, verbose_name="Заметки")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.first_name if self.first_name else self.email

    class Meta:
        db_table = "base_page_site_visitor"
        verbose_name = "Посетитель сайта"
        verbose_name_plural = "Посетители сайта"


class CarBody(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Тип автомобиля')
    img = models.ImageField(upload_to="img-car-body", null=True, blank=True, verbose_name="Изображение")
    car_id = models.IntegerField(null=True, blank=True, verbose_name="ID автомобиля")

    def __str__(self):
        return self.name if self.name else "Без названия"

    class Meta:
        db_table = "car_body"
        verbose_name = "Тип кузова автомобиля"
        verbose_name_plural = "Типы кузовов автомобилей"


class CarMark(models.Model):
    name = models.CharField(max_length=255, verbose_name="Марка автомобиля")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_mark"
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"


class CarModel(models.Model):
    mark = models.ForeignKey('CarMark', on_delete=models.CASCADE, verbose_name="Марка автомобиля", related_name="models")
    name = models.CharField(max_length=255, verbose_name="Модель автомобиля")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_model"
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"


class CarModification(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название модификации")
    mark = models.ForeignKey('CarMark', on_delete=models.CASCADE, verbose_name="Марка автомобиля",
        related_name="modifications")
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE, verbose_name="Модель автомобиля",
        related_name="modifications")
    body = models.CharField(max_length=255, verbose_name="Тип кузова")
    generation_name = models.CharField(max_length=255, verbose_name="Поколение")
    fuel = models.CharField(max_length=255, verbose_name="Тип топлива")
    tKppType = models.CharField(max_length=255, verbose_name="Тип КПП")

    def __str__(self):
        return f"{self.name} ({self.generation_name})" if self.name else f"{self.generation_name}"

    class Meta:
        db_table = "car_modification"
        verbose_name = "Модификация автомобиля"
        verbose_name_plural = "Модификации автомобилей"


class CarService(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    services_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Без названия"

    class Meta:
        db_table = 'car_services'
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class BasePageSideMenu(models.Model):
    img_evacuation = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Эвакуация")
    img_contacts = models.ImageField(upload_to="img-social", blank=True, null=True, verbose_name="Контакты")
    img_email = models.ImageField(upload_to="img-social", blank=True, null=True, verbose_name="Почта")
    img_phone = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Телефон")
    img_remont = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Ремонт")
    img_diagnostics = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Диагностика")
    img_shin_service = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Шиномонтаж")

    def __str__(self):
        return "Боковое меню"
    
    class Meta:
        db_table = "base_page_side_menu"
        verbose_name = "Боковое меню"
        verbose_name_plural = "Боковое меню"


class BasePageAddOrderServiceModal(models.Model):
    img = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Изображение")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "base_page_add_order_service_modal"
        verbose_name = "Модальное окно"
        verbose_name_plural = "Модальные окна"


class BasePageAddOrderServiceModalForm(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    call_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    date_time_order = models.DateTimeField(verbose_name="Дата и время заказа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        db_table = "base_page_add_order_service_modal_form"
        verbose_name = "Форма запись на техническое обслуживание"
        verbose_name_plural = "Формы записи на техническое обслуживание"


class BasePageHeader(models.Model):
    img_logo = models.ImageField(upload_to="img-logo", blank=True, null=True, verbose_name="Логотип")
    img_qr_code = models.ImageField(upload_to="img-qr-codes", blank=True, null=True, verbose_name="QR-код")
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Телефон")
    town_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес")
    worktime = models.CharField(max_length=255, blank=True, null=True, verbose_name="Время работы")

    def __str__(self):
        return "Хедер"

    class Meta:
        db_table = "base_page_header"
        verbose_name = "Хедер"
        verbose_name_plural = "Хедер"


class BasePageNotification(models.Model):
    img = models.ImageField(upload_to="img", blank=True, null=True, verbose_name="Изображение")
    notification_text = models.TextField(blank=True, null=True, verbose_name="Текст уведомления")
    action_text = models.TextField(blank=True, null=True, verbose_name="Текст действия")

    def __str__(self):
        return "Уведомление"
    
    class Meta:
        db_table = "base_page_notification"
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"


class BasePageFooterImage(models.Model):
    img = models.ImageField(upload_to="img-logo", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return "Изображение логотипа в футере"

    class Meta:
        db_table = "base_page_footer_image"
        verbose_name = "Изображение в футере"
        verbose_name_plural = "Изображения в футере"


class BasePageSocialImages(models.Model):
    img = models.ImageField(upload_to="img-social", blank=True, null=True, verbose_name="Изображение")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return "Социальные сети"

    class Meta:
        db_table = "base_page_social_images"
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"


class BasePageFooter(models.Model):
    img_logo = models.ImageField(upload_to="img-logo", blank=True, null=True, verbose_name="Логотип")
    text = models.TextField(blank=True, null=True, verbose_name="Текст")
    pay_icon_cash = models.ImageField(upload_to="img-pay-method", blank=True, null=True, verbose_name="Иконка наличных")
    pay_icon_mastercard = models.ImageField(upload_to="img-pay-method", blank=True, null=True, verbose_name="Иконка Mastercard")
    pay_icon_visa = models.ImageField(upload_to="img-pay-method", blank=True, null=True, verbose_name="Иконка Visa")
    pay_icon_sber = models.ImageField(upload_to="img-pay-method", blank=True, null=True, verbose_name="Иконка Сбер")
    pay_icon_halva = models.ImageField(upload_to="img-pay-method", blank=True, null=True, verbose_name="Иконка Халва")

    def __str__(self):
        return "Футер"

    class Meta:
        db_table = "base_page_footer"
        verbose_name = "Футер"
        verbose_name_plural = "Футер"
