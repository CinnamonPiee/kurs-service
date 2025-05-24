from django.db import models


class PriceShodRazvalCategory(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name='Slug')
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'price_shod_razval_category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        

class PriceShodRazvalPrice(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Тип')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    sub_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Подназвание')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to='img-car-body', null=True, blank=True, verbose_name='Изображение')
    price = models.CharField(max_length=255, blank=True, null=True, verbose_name='Цена')
    category = models.ForeignKey(PriceShodRazvalCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'price_shod_razval_price'
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
