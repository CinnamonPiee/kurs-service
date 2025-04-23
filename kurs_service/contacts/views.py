from django.shortcuts import render
from contacts.models import (
	ContactsDataContacts,
	ContactsDetailsAndContacts,
	ContactsSchemeAndDetails,
	ContactsSchemeImage,
	ContactsSliderImages,
	ContactsTitles,
	ContactsWeekdayWorkingTime,
)


def contacts(request):
	context = {
		'title': 'Контакты | OOO "КУРС"',
		'contacts_data_contacts_qr_codes': ContactsDataContacts.objects.first(),
		'contacts_data_contacts_mail': ContactsDataContacts.objects.all()[1],
		'contacts_data_contacts_address': ContactsDataContacts.objects.all()[2],
		'contacts_data_contacts': ContactsDataContacts.objects.all()[3],
		'contacts_data_contacts_wa': ContactsDataContacts.objects.all()[4],
		'contacts_data_contacts_mobile_number': ContactsDataContacts.objects.last(),
		'contacts_details_and_contacts': ContactsDetailsAndContacts.objects.all(),
		'contacts_scheme_and_details': ContactsSchemeAndDetails.objects.all(),
		'contacts_scheme_image': ContactsSchemeImage.objects.first(),
		'contacts_slider_images': ContactsSliderImages.objects.first(),
		'contacts_titles': ContactsTitles.objects.first(),
		'contacts_weekday_working_time_all': ContactsWeekdayWorkingTime.objects.all(),
		'contacts_weekday_working_time': ContactsWeekdayWorkingTime.objects.all()[:5],
		'contacts_weekday_working_time_all_day_off': ContactsWeekdayWorkingTime.objects.all()[5:],
	}
	return render(request, "contacts/contacts.html", context=context)