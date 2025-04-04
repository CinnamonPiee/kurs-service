from django.shortcuts import render
from contacts.models import (
    ContactsImages,
    ContactsWorkingTime,
    ContactsCompanyData,
    ContactsCompanyDetails,
    ContactsDirectionSchema,
    ContactsTitles,
    ContactsMapSchema,
)


def contacts(request):
    context = {
        'title': 'Контакты | OOO "КУРС"',
        'contacts_images': ContactsImages.objects.first(),
        'contacts_working_time': ContactsWorkingTime.objects.all()[:4],
        'contacts_working_time_weekend': ContactsWorkingTime.objects.all()[5:],
        'contacts_company_data': ContactsCompanyData.objects.first(),
        'contacts_company_details': ContactsCompanyDetails.objects.first(),
        'contacts_direction_schema': ContactsDirectionSchema.objects.all(),
        'contacts_map_schema': ContactsMapSchema.objects.first(),
        'contacts_titles': ContactsTitles.objects.first(),
    }
    return render(request, "contacts/contacts.html", context=context)
