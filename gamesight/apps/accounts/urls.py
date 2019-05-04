from django.conf.urls import url

from gamesight.apps.accounts.views import SelectSubscriptionView


app_name = 'accounts'

urlpatterns = [
    url(r'^select-subscription', SelectSubscriptionView.as_view(), name='select-subscription'),
]
