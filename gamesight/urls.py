"""gamesight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView

from gamesight.apps.accounts.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^app/', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('gamesight.apps.accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('r^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
