from django.db import models


class ShodRazvalCategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    translit = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "shod_razval_category"
        

class ShodRazvalPrice(models.Model):
    type = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    img = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    category_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
	
    class Meta:
        db_table = 'shod_razval_price'
        