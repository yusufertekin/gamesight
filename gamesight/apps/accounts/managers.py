from django.contrib.auth.models import BaseUserManager


class EmailUserManager(BaseUserManager):
    """
    Overriding BaseUserManager in order to allow users to register and authenticate by using email instead of username.
    """
    def create_user(self, email, password, name, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email,
                          **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, name='gamesight', **extra_fields)
