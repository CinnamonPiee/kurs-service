from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_reviews = models.CharField(max_length=255, blank=True, null=True)
    img_reviews = models.CharField(max_length=255, blank=True, null=True)
    user_reviews = models.TextField(blank=True, null=True)
    admin_reviews = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user_name}"

    class Meta:
        db_table = "reviews"
