from .models import BasePageFooter


def base_page(request):
    return {
        "base_page_footer": BasePageFooter.objects.first(),
    }