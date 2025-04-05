from django.shortcuts import render
from diagnostics.models import (
	DiagnosticsMainDirections,
	DiagnosticsWikiText,
)


def diagnostics(request):
    context = {
        'title': 'Диагностика | OOO "КУРС"',
        'diagnostics_main_directions': DiagnosticsMainDirections.objects.all(),
        'diagnostics_wiki_text': DiagnosticsWikiText.objects.all(),
    }
    return render(request, "diagnostics/diagnostics.html", context=context)
