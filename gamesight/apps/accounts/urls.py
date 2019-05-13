from django.conf.urls import url
from django.views.generic import TemplateView

from gamesight.apps.accounts.views import RegisterView, SubscriptionListView, logout_user


app_name = 'accounts'

urlpatterns = [
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^subscriptions', SubscriptionListView.as_view(), name='subscriptions'),
    url(r'^helpme', TemplateView.as_view(template_name='accounts/helpme.html'), name='helpme'),
    url(r'^logout', logout_user, name='logout'),
]
