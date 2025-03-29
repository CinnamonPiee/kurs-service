from django.db import models


class DrivingDirection(models.Model):
    img_line_metro = models.CharField(max_length=255, blank=True, null=True)
    img_train = models.CharField(max_length=255, blank=True, null=True)
    description_train = models.CharField(max_length=255, blank=True, null=True)
    img_foot = models.CharField(max_length=255, blank=True, null=True)
    description_foot = models.CharField(max_length=255, blank=True, null=True)
    img_taxi = models.CharField(max_length=255, blank=True, null=True)
    description_taxi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Направление {self.id}"

    class Meta:
        db_table = "driving_directions"
        