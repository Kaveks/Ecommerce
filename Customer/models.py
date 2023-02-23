from django.db import models

# Create your models here.
from django.db import models
import datetime as dt
import uuid
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _  # for any translations

# Create your models here.


class Customer(models.Model):
    # user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='customer',
                                on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return f" Customer name: {self.name}"


# a universal address which can either be billing or shipping address
ADDRESS_CHOICES = (
    ("B", "Billing"),
    ("S", "Shipping"),
)


class Address(models.Model):
    """
    Address
    """
# for security reasons use uuidfield which is a prolonged string hard to guess
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, related_name=_(
        "customers"), verbose_name=_("Customer"), on_delete=models.CASCADE)
    email = models.EmailField(_('email address'),
                              max_length=255, help_text=_('Required '))
    phone = models.CharField(
        _("Phone Number"), max_length=50, help_text=_('Required '))
    zipcode = models.CharField(
        _("Postcode"), max_length=50, blank=True, help_text=_('Optional '))
    address_line = models.CharField(
        _("Address 1"), max_length=255, blank=True, help_text=_('Optional '))
    address_line2 = models.CharField(
        _("Address2"), max_length=255, blank=True, help_text=_('Optional '))
    country = CountryField(multiple=False,)
    town_city = models.CharField(
        _("Town/City/State"), max_length=255, help_text=_('Required '))
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    created_at = models.DateTimeField(_("Created at"), default=now)
    updated_at = models.DateTimeField(_("Updated at"), default=now)
    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = " Customer Address"
        verbose_name_plural = "Customer Addresses"

    def __str__(self):
        return f"{self.customer.name} address"
