from django.db import models


class TOCategory(models.Model):
    parent_id = models.IntegerField(null=True, blank=True)  # Добавляем поле parent_id, которое может быть пустым
    translate_category = models.CharField(max_length=255, blank=True, null=True)
    title_category = models.CharField(max_length=255, blank=True, null=True)
    img_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title_category

    class Meta:
        db_table = "t_o_category"


class TOPrice(models.Model):
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
        db_table = "t_o_price"
