from django.shortcuts import render
from .models import (
	DiagnosticsComputerOfCars,
	DiagnosticsSuspension,
	DiagnosticsGearbox,
	DiagnosticsComputerGoals,
	DiagnosticsStager,
	DiagnosticsTitles,
	DiagnosticsWhenToGet,
)


def diagnostics(request):
	context = {
		"title": 'Диагностика | OOO "КУРС"',
		'diagnostics_computer_of_cars': DiagnosticsComputerOfCars.objects.first(),
		'diagnostics_suspension': DiagnosticsSuspension.objects.first(),
		'diagnostics_gearbox': DiagnosticsGearbox.objects.first(),
		'diagnostics_computer_goals': DiagnosticsComputerGoals.objects.first(),
		'diagnostics_stager': DiagnosticsStager.objects.first(),
		'diagnostics_titles': DiagnosticsTitles.objects.first(),
		'diagnostics_when_to_get': DiagnosticsWhenToGet.objects.first(),
	}

	return render(request, 'diagnostics/diagnostics.html', context)
