from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from gamesight.apps.accounts.managers import EmailUserManager


class EmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(_('organization name'), max_length=127)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.email


@receiver(post_save, sender=EmailUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, credit=0)


class Profile(models.Model):
    user = models.OneToOneField(EmailUser, on_delete=models.CASCADE, related_name='profile')
    credit = models.DecimalField(max_digits=7, decimal_places=2)

    def create_subscription(self, subscription_plan):
        subscription = Subscription(subscription_plan=subscription_plan,
                                    profile=self)
        subscription.save()
        return subscription


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(help_text=_('Detailed explanation of subscription plan'))
    recurring_credits = models.DecimalField(max_digits=6, decimal_places=2)
    num_project_allowence = models.IntegerField()
    num_saved_report_allowence = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Subscription(models.Model):
    subscription_plan = models.ForeignKey(SubscriptionPlan, null=True, blank=True, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_canceled = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.profile.credit += self.subscription_plan.recurring_credits
        self.profile.save()

    @property
    def is_active(self):
        return not date_canceled
