from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    date_time = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Новость"

    class Meta:
        db_table = "news"
        