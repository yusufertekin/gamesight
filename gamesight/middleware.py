from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url, settings.STATIC_URL] + \
                         getattr(settings, 'OPEN_URLS', [])

    def __call__(self, request):
        if not request.user.is_authenticated \
        and not request.path_info.startswith('/static/') \
        and not request.path_info in self.open_urls:
            return redirect(self.login_url+'?next='+request.path)

        return self.get_response(request)
