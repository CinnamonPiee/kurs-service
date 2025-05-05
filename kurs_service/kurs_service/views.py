from django.http import HttpResponse

def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /site/signup
    Disallow: /site/login
    Disallow: /site/request-password-reset?class=kurs-checkbox
    Disallow: /admin
    Sitemap: https://kurs-service.ru/sitemap.xml
    """
    return HttpResponse(content, content_type="text/plain")