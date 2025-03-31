from django.shortcuts import render
from about.models import (
    DescriptionCompany,
    Advantages,
    BestInBusiness,
    Contacts,
    AccuratelyTime,
	Training,
    AboutHeaders,
)


def about(request):
    context = {
        'title': 'О сервисе | OOO "КУРС"',
        'description_company_text': DescriptionCompany.objects.last(),
        'advantages_text': Advantages.objects.all(),
        'best_in_business': BestInBusiness.objects.last(),
        'contacts': Contacts.objects.all(),
        'accurately_time': AccuratelyTime.objects.last(),
        'training_img': Training.objects.all(),
        'about_headers': AboutHeaders.objects.last(),
    
    }
    return render(request, "about/about.html", context=context)
