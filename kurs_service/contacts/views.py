from django.shortcuts import render
from contacts.models import (
    SupportHelp,
    WorkingTime,
    ContactsData,
    ContactsAndDetails,
    DirectionScheme,
    ContactsHeaders,
)


def contacts(request):
    context = {
        'title': 'Контакты | OOO "КУРС"',
        'support_help': SupportHelp.objects.last(),
        'working_time': WorkingTime.objects.all(),
        'contacts_data': ContactsData.objects.all(),
        'contacts_and_details': ContactsAndDetails.objects.last(),
        'direction_scheme': DirectionScheme.objects.all(),
        'contacts_headers': ContactsHeaders.objects.last(),
    }
    return render(request, "contacts/contacts.html", context=context)
