from django.shortcuts import render
from about.models import (
	AboutAccuratelyInTime,
	AboutBestInBusiness,
	AboutContacts,
	AboutHowWeTrainingStaff,
	AboutLetsAcquainted,
	AboutOurAdvantages,
	AboutTitles,
)


def about(request):
	context = {
		'title': 'О сервисе | OOO "КУРС"',
		'about_accurately_in_time': AboutAccuratelyInTime.objects.first(),
		'about_best_business': AboutBestInBusiness.objects.first(),
		'about_contacts_email': AboutContacts.objects.first(),
		'about_contacts_number': AboutContacts.objects.all()[1],
		'about_contacts': AboutContacts.objects.all()[2:],
		'about_how_we_training_staff': AboutHowWeTrainingStaff.objects.all(),
		'about_lets_acquainted': AboutLetsAcquainted.objects.first(),
		'about_our_advantages': AboutOurAdvantages.objects.all(),
		'about_titles': AboutTitles.objects.first(),
	}
	return render(request, "about/about.html", context=context)
