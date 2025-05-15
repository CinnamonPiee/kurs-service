from django.shortcuts import render


def check_list(request):
	context = {}

	return render(request, 'check_list/check_list.html', context)
