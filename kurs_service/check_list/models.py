from django.db import models


class CheckList(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    services_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "check_list"
        

class OrderCheckList(models.Model):
    name_user = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    car_mark = models.CharField(max_length=255, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    car_modification = models.CharField(max_length=255, blank=True, null=True)
    comment_user = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)
    status_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_user} - {self.car_mark} {self.car_model}"

    class Meta:
        db_table = "order_check_list"
        

class OrderCheckListItems(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} (Order ID: {self.order_id})"

    class Meta:
        db_table = "order_check_list_items"
