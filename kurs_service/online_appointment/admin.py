from django.contrib import admin
from .models import (
	OnlineAppointmentSliderImages,
	OnlineAppointmentTitles,
	OnlineAppointmentForm,
)


@admin.register(OnlineAppointmentSliderImages)
class OnlineAppointmentSliderImagesAdmin(admin.ModelAdmin):
	pass


@admin.register(OnlineAppointmentTitles)
class OnlineAppointmentTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(OnlineAppointmentForm)
class OnlineAppointmentFormAdmin(admin.ModelAdmin):
	pass
