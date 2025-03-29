from django.db import models


class TireFittingCategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    translit = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tire_fitting_category"


class TireFittingPrice(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    category_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tire_fitting_price"
