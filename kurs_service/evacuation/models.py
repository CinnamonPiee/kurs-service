from django.db import models


class EvacuationCondition(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Условие эвакуации"

    class Meta:
        db_table = "evacuation_conditions"
        

class PriceEvacuationService(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.price}"

    class Meta:
        db_table = "price_evacuation_services"
        

class PriceEvacuationText(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    auto = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.auto} - {self.price}"

    class Meta:
        db_table = "price_evacuation_text"
        

class OrderEvacuation(models.Model):
    title_service = models.CharField(max_length=255, blank=True, null=True)
    name_user = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    car_body = models.CharField(max_length=255, blank=True, null=True)
    comment_user = models.TextField(blank=True, null=True)
    data_time_order = models.CharField(max_length=255, blank=True, null=True)
    address_user = models.CharField(max_length=255, blank=True, null=True)
    payment = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Order for {self.name_user} - {self.title_service}"

    class Meta:
        db_table = "order_evacuation"
