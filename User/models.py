from django.db import models

# Create your models here.

# Create a complete user account

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _  # for any translations
import datetime
from django.utils import timezone

# specify how user data is to be saves in database


class UserAccountManager(BaseUserManager):
    # creating supper user
    def create_superuser(self, email, user_name, password, **other_fields):
        # set to true the following
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        # restrictions
        if other_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be a staff')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must be assigned is_superuser to True')
        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError(_('you must provide a valid email address!'))
        if not password:
            raise ValueError(_('you must provide a valid password'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
# create a complete new user login system but inherit the django one


class Account(AbstractBaseUser, PermissionsMixin):
    # actual login unique identifier,as opposed to django's username
    email = models.EmailField(_('email address'), unique=True,
                              max_length=255, help_text=_('Required '))
    user_name = models.CharField(
        _('user name'), max_length=200, unique=True,help_text=_('Required'))
    last_name = models.CharField(
        _('last name'), max_length=200, null=True, help_text=_('Required '))
    phone = models.CharField(
        _('phone'), max_length=200, null=True, help_text=_('Required '))
    # user status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    now = timezone.make_aware(datetime.datetime.now(),
                              timezone.get_default_timezone())
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)
    # manager user data saving
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]  # will popup to be filled by user

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return '{}'.format(self.user_name)
