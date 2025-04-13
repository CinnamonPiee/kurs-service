from django.shortcuts import render
from photo_gallery.models import (
	PhotoGalleryImages,
	PhotoGalleryTitles,
)


def photo_gallery(request):
	context = {
		'title': 'Фото-галерея | OOO "КУРС"',
		'photo_gallery_images': PhotoGalleryImages.objects.all(),
		'photo_gallery_titles': PhotoGalleryTitles.objects.first(),
	}
	return render(request, "photo_gallery/photo_gallery.html", context=context)
