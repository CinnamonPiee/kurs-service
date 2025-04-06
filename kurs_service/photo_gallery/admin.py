from django.contrib import admin
from photo_gallery.models import (
    PhotoGalleryImages,
    PhotoGalleryTitles,
)


@admin.register(PhotoGalleryImages)
class PhotoGalleryImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(PhotoGalleryTitles)
class PhotoGalleryTitlesAdmin(admin.ModelAdmin):
	pass
