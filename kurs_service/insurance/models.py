from django.db import models


class InsuranceAdvantage(models.Model):
    icon_advantages = models.CharField(max_length=255, blank=True, null=True)
    title_advantages = models.CharField(max_length=255, blank=True, null=True)
    content_advantages = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_advantages if self.title_advantages else "Преимущество страховки"

    class Meta:
        db_table = "insuranse_advantages"
        

class InsuranceQuestion(models.Model):
    title_questions = models.CharField(max_length=255, blank=True, null=True)
    content_questions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_questions if self.title_questions else "Вопрос страховки"

    class Meta:
        db_table = "insuranse_questions"
        

class OrderInsurance(models.Model):
    name_user = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    call_number = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    driving_experience = models.IntegerField(blank=True, null=True)
    person_sex = models.CharField(max_length=255, blank=True, null=True)
    date_time_insurance = models.CharField(max_length=255, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    status_insurance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Insurance Order for {self.name_user}"

    class Meta:
        db_table = "order_insurance"
