from django.db import models


class Discount(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.CharField(max_length=255, blank=True, null=True)  # Можно заменить на DateField, если дата
    date_stop = models.CharField(max_length=255, blank=True, null=True)   # будет в формате даты

    def __str__(self):
        return self.title if self.title else "Скидка"

    class Meta:
        db_table = "discounts"
