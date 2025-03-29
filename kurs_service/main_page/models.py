from django.db import models


class AddressCompany(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    weekdays = models.CharField(max_length=255, blank=True, null=True)
    output = models.CharField(max_length=255, blank=True, null=True)
    saturday = models.CharField(max_length=255, blank=True, null=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)
    text_qr = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.address if self.address else "Адрес компании"

    class Meta:
        db_table = "address_company"
        

class DirectionActivity(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Направление деятельности"

    class Meta:
        db_table = "direction_activity"
        

class HomeAdvantage(models.Model):
    icon_advantage = models.CharField(max_length=255, blank=True, null=True)
    title_advantage = models.CharField(max_length=255, blank=True, null=True)
    content_advantage = models.TextField(blank=True, null=True)
    short_content_advantage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_advantage if self.title_advantage else "Преимущество"

    class Meta:
        db_table = "home_advantages"
        

class MainQuestion(models.Model):
    title_questions = models.CharField(max_length=255, blank=True, null=True)
    content_questions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_questions if self.title_questions else "Основной вопрос"

    class Meta:
        db_table = "main_questions"
        

class PagesData(models.Model):
    title_pages = models.CharField(max_length=255, blank=True, null=True)
    keywords_pages = models.CharField(max_length=255, blank=True, null=True)
    description_pages = models.CharField(max_length=255, blank=True, null=True)
    route_pages = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title_pages

    class Meta:
        db_table = "pages_data"
