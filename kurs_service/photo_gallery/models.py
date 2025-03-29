from django.db import models


class PhotoGallery(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    photo_name = models.CharField(max_length=255, blank=True, null=True)
    photo_name_min = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description if self.description else "Фото"

    class Meta:
        db_table = "photo_gallery"
