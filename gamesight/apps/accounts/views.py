from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView


class LoginRegisterView(TemplateView):
    tempalate_name = 'accounts/login_register.html'

    def post(self, request, *args, **kwargs):
        is_register = request.POST.get('is_register')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if is_register:
            organization_name = request.POST.get('organization_name')
            if email and password and organization_name:
                user = settings.AUTH_USER_MODEL.objects.create_user(email=email, password=password, name=organization_name)
                user.save()
                user = authenticate(email=email, password=password)
                return HttpResponseRedirect(reverse_lazy('accounts:select-subscription'))
            else:
                return render_to_response({'error_message': 'Please fill all required fields'})

        else:
            if email and password:
                user_cache = authenticate(email=email, password=password)
                if self.user_cache is None:
                    return render_to_response({'error_message': 'Please use correct email and password'})
                else:
                    return render_to_response(reverse_lazy('site-home'))
                
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            next = request.REQUEST.get('next', None)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse_lazy('site-home'))

            return self.render_to_response(context)


class SelectSubscriptionView(TemplateView):
    template_name = 'accounts/select_subscription.html'

    def get_context_data(self):
        return {
            'free_subscription_plan': SubscriptionPlan.objects.get(id=0),
            'paid_subscription_plans': SubscriptionPlan.objects.filter(id__gt=0),
        }

    def post(self, request, *args, **kwargs):
        selected_subscription_plan = SubscriptionPlan.objects.get(name=request.POST.get('selected_subscription'))
        request.user.profile.create_subscription(selected_subscription_plan)
        return render_to_response(reverse_lazy('site-home'))
