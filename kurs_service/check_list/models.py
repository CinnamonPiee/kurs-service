from django.db import models


class CheckListOrder(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    number = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    car_mark = models.CharField(max_length=255, verbose_name="Марка автомобиля")
    car_model = models.CharField(max_length=255, verbose_name="Модель автомобиля")
    car_modification = models.CharField(max_length=255, verbose_name="Модификация", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)
    date_time_order = models.DateTimeField(verbose_name="Дата и время заказа")
    comment_user = models.TextField(verbose_name="Комментарий пользователя", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.created_at})"

    class Meta:
        db_table = 'check_list_order'
        verbose_name = "Заказ чек-листа"
        verbose_name_plural = "Заказы чек-листа"

class CheckListOrderItem(models.Model):
    order = models.ForeignKey(CheckListOrder, on_delete=models.CASCADE, related_name="items")
    service_id = models.PositiveIntegerField(verbose_name="ID услуги")
    service_name = models.CharField(max_length=255, verbose_name="Название услуги")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return f"{self.service_name} x{self.quantity}"

    class Meta:
        db_table = 'check_list_order_item'
        verbose_name = "Позиция заказа чек-листа"
        verbose_name_plural = "Позиции заказа чек-листа"


class CheckListTitles(models.Model):
	your_check_list = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ваш чек лист')
	making_an_appointment_for_service = models.CharField(max_length=255, null=True, blank=True, verbose_name='Оформление записи на сервис')

	def __str__(self):
		return 'Заголовки'

	class Meta:
		db_table = 'check_list_titles'
		verbose_name = 'Заголовок'
		verbose_name_plural = 'Заголовки'
