from django.db import models


class DescriptionCompany(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Описание компании"

    class Meta:
        db_table = "description_company"
        

class Training(models.Model):
    img = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description

    class Meta:
        db_table = "training"
