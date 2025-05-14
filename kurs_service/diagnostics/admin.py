from django.contrib import admin
from .models import (
	DiagnosticsComputerOfCars,
	DiagnosticsSuspension,
	DiagnosticsGearbox,
	DiagnosticsComputerGoals,
	DiagnosticsStager,
	DiagnosticsTitles,
	DiagnosticsWhenToGet,
)


@admin.register(DiagnosticsComputerOfCars)
class DiagnosticsComputerOfCarsAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsSuspension)
class DiagnosticsSuspensionAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsGearbox)
class DiagnosticsGearboxAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsComputerGoals)
class DiagnosticsComputerGoalsAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsStager)
class DiagnosticsStagerAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsTitles)
class DiagnosticsTitlesAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsWhenToGet)
class DiagnosticsWhenToGetAdmin(admin.ModelAdmin):
	pass
