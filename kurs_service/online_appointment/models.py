from django.db import models


class CarBody(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    car_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "car_body"
        

class CarMark(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_mark"
        

class CarModel(models.Model):
    mark = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_model"


class CarModification(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    mark = models.ForeignKey(CarMark, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    generation_name = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    tKppType = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car_modification"
        

class OnlineAppointment(models.Model):
    name_user = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment_user = models.TextField(blank=True, null=True)
    title_services = models.CharField(max_length=255, blank=True, null=True)
    car_mark = models.CharField(max_length=255, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    car_modification = models.CharField(max_length=255, blank=True, null=True)
    car_body = models.CharField(max_length=255, blank=True, null=True)
    date_time_order = models.CharField(max_length=255, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name_user} - {self.title_services}"

    class Meta:
        db_table = "online_appointment"
        

class OrderPrice(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    price_id = models.IntegerField(blank=True, null=True)
    title_price = models.CharField(max_length=255, blank=True, null=True)
    name_user = models.CharField(max_length=255, blank=True, null=True)
    comment_user = models.TextField(blank=True, null=True)
    date_time_order = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Order Price for {self.name_user} - {self.title_price}"

    class Meta:
        db_table = "order_price"
        

class OrderServicesModal(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    title_service = models.CharField(max_length=255, blank=True, null=True)
    name_user = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True)
    comment_user = models.CharField(max_length=255, blank=True, null=True)
    date_time_order = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Order Service for {self.name_user} - {self.title_service}"

    class Meta:
        db_table = "order_services_modal"
