from django.db import models


class DrivingDirection(models.Model):
    img_line_metro = models.ImageField(upload_to="passage_and_travel_scheme", blank=True, null=True, verbose_name="Изображение")
    img_train = models.ImageField(upload_to="passage_and_travel_scheme", blank=True, null=True, verbose_name="Изображение")
    description_train = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    img_foot = models.ImageField(upload_to="passage_and_travel_scheme", blank=True, null=True, verbose_name="Изображение")
    description_foot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    img_taxi = models.ImageField(upload_to="passage_and_travel_scheme", blank=True, null=True, verbose_name="Изображение")
    description_taxi = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.description_train

    class Meta:
        db_table = "driving_directions"
        verbose_name: str = "направление"
        verbose_name_plural: str = "Направления"
