from django.shortcuts import render
from django.http import JsonResponse


def check_list(request):
	context = {}

	return render(request, 'check_list/check_list.html', context)


def check_list_count(request):
    count = 0
    return JsonResponse({'count': count})
