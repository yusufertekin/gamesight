from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from gamesight.apps.accounts.models import SubscriptionPlan


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user_cache = authenticate(email=email, password=password)
            if user_cache is None:
                return self.render_to_response({'error_message': 'Please use correct email and password'})
            else:
                login(request, user_cache)
                return HttpResponseRedirect(reverse_lazy('site-home'))
                
    
    def get(self, request, *args, **kwargs):
        next = request.GET.get('next', None)
        if request.user.is_authenticated:
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse_lazy('site-home'))

        return self.render_to_response({'next': next})


class RegisterView(TemplateView):
    template_name = 'accounts/register.html'

    def get_context_data(self, **kwargs):
        context = {
            'free_subscription_plan': SubscriptionPlan.objects.get(id=1),
            'paid_subscription_plans': SubscriptionPlan.objects.filter(id__gt=1),
        }
        context.update(kwargs)
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        organization_name = request.POST.get('organization_name')
        if email and password and password2 and organization_name:
            if password != password2:
                return self.render_to_response(self.get_context_data(error_message='Password does not match'))
            user = get_user_model().objects.create_user(email=email, password=password, name=organization_name)
            user.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            user.profile.create_subscription(SubscriptionPlan.objects.first())
            return HttpResponseRedirect(reverse_lazy('site-home'))
        else:
            return self.render_to_response(self.get_context_data(error_message='Please fill all required fields'))


class SubscriptionListView(TemplateView):
    template_name = 'accounts/subscriptions.html'

    def get_context_data(self, **kwargs):
        context = {
            'paid_subscription_plans': SubscriptionPlan.objects.filter(id__gt=1),
        }
        context.update(kwargs)
        return context


def logout_user(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))
