from django.conf.urls import url

from gamesight.apps.accounts.views import RegisterView, logout_user


app_name = 'accounts'

urlpatterns = [
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^logout', logout_user, name='logout'),
]
