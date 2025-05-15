from django.shortcuts import render


def online_appointment(request):
	context = {}

	return render(request, 'online_appointment/online_appointment.html', context)
