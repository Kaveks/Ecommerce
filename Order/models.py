from django.db import models
from Customer.models import Customer, Address
from Store.models import Item
from django.utils import timezone
import datetime as dt

# Create your models here.


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    date = models.DateTimeField(default=now)

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return f"{self.quantity} of {self.item.title} ordered"


class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    date_ordered = models.DateTimeField(default=now)
    ordered = models.BooleanField(default=False)
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

    # sum all orderitem price
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
            # subract coupon amount if the user has it
            if self.coupon:
                total -= self.coupon.amount
        return total

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    now = timezone.make_aware(dt.datetime.now(),
                              timezone.get_default_timezone())
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username


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
