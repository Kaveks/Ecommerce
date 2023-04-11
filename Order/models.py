from django.db import models
from Customer.models import Address
from django.conf import settings
from Store.models import Item
from Customer.models import Customer
from django.utils import timezone
import datetime as dt

from django.db.models.signals import post_save
from Customer.models import Customer

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    #name=models.CharField(max_length=255,null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)
    class Meta:
        verbose_name ='User Profile'
        verbose_name_plural ='User Profiles'
        

    def __str__(self):
        return f"Stripe payments from: {self.user.first_name}"


 
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False,verbose_name=('Order completed'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    date = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Ordered Item'
        verbose_name_plural = 'Ordered Items'
        ordering = ('-date',)

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return float(self.get_total_item_price()) - float(self.get_total_discount_item_price())

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return f"{self.quantity} of {self.item.title} ordered by : {self.user.first_name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    date_ordered = models.DateTimeField(default=now)
    ordered = models.BooleanField(default=False,verbose_name=('Order completed'))
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    shippingAddress = models.ForeignKey(
        Address,
        related_name="shippingAddress",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    billingAddress = models.ForeignKey(
        Address,
        related_name="billingAddress",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    payment = models.ForeignKey(
        "Payment", on_delete=models.SET_NULL, blank=True, null=True
    )
    coupon = models.ForeignKey(
        "Coupon", on_delete=models.SET_NULL, blank=True, null=True
    )
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    """
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received by client
    6. Refunds
    """
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-date_ordered',)
    # sum all orderitem price
    def get_total(self):
        total = 0
        for order_item in self.items.all():
           total += float(order_item.get_final_price())
           # subract coupon amount if the user has it
           if self.coupon:
                total -= self.coupon.amount
        return total

    def __str__(self):
        return f"Order made by : {self.user.first_name}"


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.first_name


# create discount codes
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    refund_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.pk}"



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile=UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)