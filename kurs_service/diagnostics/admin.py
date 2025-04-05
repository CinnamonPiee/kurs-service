from django.contrib import admin
from diagnostics.models import (
	DiagnosticsMainDirections,
	DiagnosticsWikiText,
)


@admin.register(DiagnosticsMainDirections)
class DiagnosticsMainDirectionsAdmin(admin.ModelAdmin):
	pass


@admin.register(DiagnosticsWikiText)
class DiagnosticsWikiTextAdmin(admin.ModelAdmin):
	pass
