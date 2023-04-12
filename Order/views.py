from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import (
    Item,
    OrderItem,
    Order,
    Payment,
    Coupon,
    Refund,
    UserProfile,
)
from Customer.models import Address
from django.utils import timezone
import datetime as dt
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .forms import (CheckoutForm, CouponForm, RefundForm, PaymentForm)
from django.http import HttpResponse,JsonResponse
import json as JSON


import random  # create random numbers
import string  # stringify the numbers
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.


def addToCart(request, slug):
    # get an item of a given slug or raise an error
    item = get_object_or_404(Item, slug=slug)
    # create OrderItem or get an already created one
    orderItem, created = OrderItem.objects.get_or_create(
        user=request.user, item=item, ordered=False)
    # get incomplete order for the user
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        # get the first order
        order = order_qs[0]
        # check if order item exist in the order
        if order.items.filter(item__slug=item.slug).exists():
            orderItem.quantity += 1
            orderItem.save()
            messages.info(request, f"{item.title} quantity was increased.")
            return redirect("Order:order-summary")
        else:
            order.items.add(orderItem)
            messages.info(request, f"{item.title} was added to your cart.")
            return redirect("Store:home",)
    else:
        now = timezone.make_aware(dt.datetime.now(),
                                  timezone.get_default_timezone())
        ordered_date = now
        order = Order.objects.create(
            user=request.user, date_ordered=ordered_date)
        # add order in the orderitem if it is non existent
        order.items.add(orderItem)
        messages.info(request, f"{item.title} was added to your cart.")
        return redirect("Store:home",)


# remove item from cart
def removeFromCart(request, slug):
    # get a particular item or raise an error'404'
    item = get_object_or_404(Item, slug=slug)
    # get incomplete  for the user
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # check whether the order exist
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in order
        if order.items.filter(item__slug=item.slug).exists():
            orderItem = OrderItem.objects.filter(
                user=request.user, item=item, ordered=False
            )[0]
            order.items.remove(orderItem)
            orderItem.delete()
            messages.info(request, f"{item.title} was removed from your cart.")
            return redirect("Order:order-summary")
        else:
            messages.info(request, f"{item.title} was not in your cart")
            return redirect("Store:product", slug=slug)
    else:
        messages.info(
            request, f"{request.user.user_name}! you do not have an active order")
        return redirect("Store:product", slug=slug)


def removeSingleItemFromCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, f"{item.title} quantity was decreased.")
            return redirect("Order:order-summary")
        else:
            messages.info(request, f"{item.title} was not in your cart")
            return redirect("Store:product", slug=slug)
    else:
        messages.info(
            request,  f"{request.user.user_name}! you do not have an active order")
        return redirect("Store:product", slug=slug)


def moveToCart(request, slug):
    # get an item of a given slug or raise an error
    item = get_object_or_404(Item, slug=slug)
    # create OrderItem or get an already created one
    orderItem, created = OrderItem.objects.get_or_create(
        user=request.user, item=item, ordered=False)
    # get incomplete order for the user
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        # get the first order
        order = order_qs[0]
        # check if order item exist in the order
        if order.items.filter(item__slug=item.slug).exists():
            orderItem.quantity += 1
            orderItem.save()
            if item.users_wishlist.filter(id=request.user.id).exists():
                item.users_wishlist.remove(request.user)

            messages.info(
                request, f"{item.title} quantity has increased since it exists in your Cart.")
            return redirect("User:wishlist")
        else:
            order.items.add(orderItem)
            if item.users_wishlist.filter(id=request.user.id).exists():
                item.users_wishlist.remove(request.user)
            messages.info(request, f"{item.title} was moved to your cart.")
            return redirect("User:wishlist",)
    else:
        now = timezone.make_aware(dt.datetime.now(),
                                  timezone.get_default_timezone())
        ordered_date = now
        order = Order.objects.create(
            user=request.user, date_ordered=ordered_date)
        # add order in the orderitem if it is non existent
        order.items.add(orderItem)
        if item.users_wishlist.filter(id=request.user.id).exists():
            item.users_wishlist.remove(request.user)
        messages.info(request, f"{item.title} was moved to your cart.")
        return redirect("User:wishlist",)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {'order': order}
            return render(self.request, 'Order/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(
                self.request, f"{self.request.user.user_name}! you do not have an active order")
            return redirect('/')


class CustomerOrderView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {"order": order}
            return render(self.request, "User/dashboard/orders.html", context)
        except ObjectDoesNotExist:
            messages.warning(
                self.request, f"{self.request.user.user_name}  you do not have any ordered items! ")
            return redirect('User:dashboard')


def is_valid_checkout_form(values):
    valid = True
    for field in values:
        if field == "":
            valid = False
    return valid


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            checkout_form = CheckoutForm()
            context = {
                "form": checkout_form,
                "order": order,
                "couponform": CouponForm(),
                "DISPLAY_COUPON_FORM": True,
            }
            # update shipping and billing addresses in the form above when user has
            # a default of either
            shippingAddress_qs = Address.objects.filter(
                customer=self.request.user,
                address_type='Shipping',
                default=True)

            if shippingAddress_qs.exists():
                context.update(
                    {'default_shipping_address': shippingAddress_qs[0]}
                )
            billingAddress_qs = Address.objects.filter(
                customer=self.request.user,
                address_type='Billing',
                default=True)

            if billingAddress_qs.exists():
                context.update(
                    {'default_billing_address': billingAddress_qs[0]}
                )
            return render(self.request, 'Order/checkout.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("Order:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            try:
                """ Shipping Information"""
                use_default_shipping_address = form.cleaned_data.get(
                    "use_default_shipping_address")
                if use_default_shipping_address:
                    print(
                        f"{self.request.user} is using default shipping information")
                    address_qs = Address.objects.filter(
                        customer=self.request.user,
                        address_type="Shipping",
                        default=True
                    )
                    # check if the user has a default shipping address
                    if address_qs.exists():
                        shippingAddress = address_qs[0]
                        order.shoppingAddress = shippingAddress
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default shipping information that is available")
                        return redirect('Order:checkout')
                else:
                    # capture new address if no default exists by populating CheckoutForm
                    print(
                        f"{self.request.user} is entering a new shipping information")
                    shipping_firstname = form.cleaned_data.get(
                        "shipping_firstname")
                    shipping_lastname = form.cleaned_data.get(
                        "shipping_lastname")
                    shipping_email = form.cleaned_data.get("shipping_email")
                    shipping_phone = form.cleaned_data.get("shipping_phone")
                    shipping_address1 = form.cleaned_data.get(
                        "shipping_address1")
                    shipping_address2 = form.cleaned_data.get(
                        "shipping_address2")
                    shipping_country = form.cleaned_data.get(
                        "shipping_country")
                    shipping_town = form.cleaned_data.get("shipping_town")
                    shipping_zipcode = form.cleaned_data.get(
                        "shipping_zipcode")

                    if is_valid_checkout_form([shipping_firstname, shipping_lastname, shipping_email, shipping_phone, shipping_address1, shipping_country, shipping_town, shipping_zipcode]):
                        shippingAddress = Address(
                            customer=self.request.user,
                            first_name=shipping_firstname,
                            last_name=shipping_lastname,
                            email=shipping_email,
                            phone=shipping_phone,
                            address=shipping_address1,
                            country=shipping_country,
                            town_city=shipping_town,
                            zipcode=shipping_zipcode,
                            address_type="Shipping"
                        )
                        shippingAddress.save()
                        # save the shipping address regardless of presence of default or not
                        order.shippingAddress = shippingAddress
                        order.save()
                        # set the entered shipping information to default up on check
                        # of set_default_shipping_address checkbox
                        set_default_shipping_address = form.cleaned_data.get(
                            'set_default_shipping_address')
                        if set_default_shipping_address:
                            shippingAddress.default = True
                            shippingAddress.save()
                    else:
                        messages.info(
                            self.request, "Please fill in the required shipping Information fields")
                        return redirect('Order:checkout')

                """ Billing information"""
                use_default_billing_address = form.cleaned_data.get(
                    'use_default_billing_address')
                # confirm whether shipping address is same as billing address
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')
                if same_billing_address:
                    billingAddress = shippingAddress
                    # clone billing to none pk
                    billingAddress.pk = None
                    billingAddress.save()
                    billingAddress.address_type = 'Billing'
                    billingAddress.save()
                    order.billingAddress = billingAddress
                    order.save()

                # if billingAddress is not assigned to be same as shipping address
                # then user is to type in the  billing information, but first
                # check if user will use the default billing address if any
                elif use_default_billing_address:
                    print("Using the default billing information")
                    address_qs = Address.objects.filter(
                        customer=self.request.user,
                        address_type='Billing',
                        default=True
                    )
                    # check if the user has a default shipping address
                    if address_qs.exists():
                        billingAddress = address_qs[0]
                        order.billingAddress = billingAddress
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default billing information available")
                        return redirect('Order:checkout')
                else:
                    print(
                        f"{self.request.user} is entering a new billing information")
                    billing_firstname = form.cleaned_data.get(
                        "billing_firstname")
                    billing_lastname = form.cleaned_data.get(
                        "billing_lastname")
                    billing_email = form.cleaned_data.get("billing_email")
                    billing_phone = form.cleaned_data.get("billing_phone")
                    billing_address1 = form.cleaned_data.get(
                        "billing_address1")
                    billing_address2 = form.cleaned_data.get(
                        "billing_address2")
                    billing_country = form.cleaned_data.get("billing_country")
                    billing_town = form.cleaned_data.get("billing_town")
                    billing_zipcode = form.cleaned_data.get("billing_zipcode")
                    if is_valid_checkout_form([billing_firstname, billing_lastname, billing_email, billing_phone, billing_address1, billing_country, billing_town, billing_zipcode]):
                        billingAddress = Address(
                            customer=self.request.user,
                            first_name=billing_firstname,
                            last_name=billing_lastname,
                            email=billing_email,
                            phone=billing_phone,
                            address=billing_address1,
                            country=billing_country,
                            town_city=billing_town,
                            zipcode=billing_zipcode,
                            address_type="Billing"
                        )
                        billingAddress.save()
                        # save the shipping address regardless of presence of default or not
                        order.billingAddress = billingAddress
                        order.save()
                        # set the entered shipping information to default up on check
                        # of set_default_shipping_address checkbox
                        set_default_billing_address = form.cleaned_data.get(
                            'set_default_billing_address')
                        if set_default_billing_address:
                            billingAddress.default = True
                            billingAddress.save()
                    else:
                        messages.info(
                            self.request, "Please fill in both the required shipping and billing  Information fields")
                        return redirect('Order:checkout')

                # pay for order now after adding shipping and billing addresses
                payment_option = form.cleaned_data.get("payment_option")
                # redirect depending on option of payment
                if payment_option == "S":
                    return redirect("Order:payment1", payment_option="Stripe")
                elif payment_option == "P":
                    return redirect("Order:payment2", payment_option="Paypal")
                elif payment_option == "M":
                    return redirect("Order:payment3", payment_option="Mpesa")
                else:
                    messages.warning(
                        self.request, "invalid payment option selected")
                    return redirect("Order:checkout")
            except ObjectDoesNotExist:
                messages.warning(
                    self.request, "You do not have an active order")
                return redirect("Order:order-summary")
        else:
            return HttpResponse('The Checkout form is invalid,Verify please!')


# create  a reference code after order payment
def create_ref_code():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=20))


class StripePaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        # if user does not have a billing address restrict going to payment page
        if order.billingAddress:
            context = {
                "order": order,
                # do not  display coupon form on the payment page
                "DISPLAY_COUPON_FORM": False,
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
            }
            userprofile = self.request.user.userprofile
            if userprofile.one_click_purchasing:
                # fetch the users card list
                cards = stripe.Customer.list_sources(
                    userprofile.stripe_customer_id,
                    limit=3,
                    object='card'
                )
                card_list = cards['data']
                if len(card_list) > 0:
                    # update the context with the default card
                    context.update({
                        'card': card_list[0]
                    })
            return render(self.request, "Order/stripe_payment.html", context)
        else:
            messages.warning(
                self.request, "You have not added a billing address")
            return redirect("Order:checkout")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = PaymentForm(self.request.POST)
        userprofile = UserProfile.objects.get(customer=self.request.user)
        if form.is_valid():
            token = form.cleaned_data.get('stripeToken')
            save = form.cleaned_data.get('save')
            use_default = form.cleaned_data.get('use_default')

            if save:
                if userprofile.stripe_customer_id != '' and userprofile.stripe_customer_id is not None:
                    customer = stripe.Customer.retrieve(
                        userprofile.stripe_customer_id)
                    customer.sources.create(source=token)

                else:
                    customer = stripe.Customer.create(
                        email=self.request.user.email,
                    )
                    customer.sources.create(source=token)
                    userprofile.stripe_customer_id = customer['id']
                    userprofile.one_click_purchasing = True
                    userprofile.save()

            amount = int(order.get_total() * 100)
            try:
                if use_default or save:
                    # charge the customer because we cannot charge the token more than once
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        customer=userprofile.stripe_customer_id
                    )
                else:
                    # charge once off on the token
                    charge = stripe.Charge.create(
                        amount=amount,  # cents
                        currency="usd",
                        source=token
                    )

                    # create the payment
                    payment = Payment()
                    payment.stripe_charge_id = charge["id"]
                    payment.user = self.request.user
                    payment.amount = order.get_total()
                    payment.save()

                    # update order items paid to ordered=True
                    order_items = order.items.all()
                    order_items.update(ordered=True)
                    for item in order_items:
                        item.save()
                    # assign payment to order
                    order.ordered = True
                    order.payment = payment
                    # assign ref_code after payment
                    order.ref_code = create_ref_code()
                    order.save()

                    messages.success(
                        self.request, "Your order was successful!")
                    return redirect("/")
                # stripe error handling
            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get("error", {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("/")

            except stripe.error.RateLimitError as e:
                # Too many requests made to the API too quickly
                messages.warning(self.request, "Rate limit error")
                return redirect("/")

            except stripe.error.InvalidRequestError as e:
                # Invalid parameters were supplied to Stripe's API
                print(e)
                messages.warning(self.request, "Invalid parameters")
                return redirect("/")

            except stripe.error.AuthenticationError as e:
                # Authentication with Stripe's API failed
                # (maybe you changed API keys recently)
                messages.warning(self.request, "Not authenticated")
                return redirect("/")

            except stripe.error.APIConnectionError as e:
                # Network communication with Stripe failed
                messages.warning(self.request, "Network error")
                return redirect("/")

            except stripe.error.StripeError as e:
                # Display a very generic error to the user, and maybe send
                # yourself an email
                messages.warning(
                    self.request,
                    "Something went wrong. You were not charged. Please try again.",
                )
                return redirect("/")

            except Exception as e:
                # send an email to ourselves to fix something
                messages.warning(
                    self.request, "A serious error occurred. We have been notified."
                )
                return redirect("/")
        messages.warning(self.request, "Invalid data received")
        return redirect("Order:payment1")


class PaypalPaymentView(View):
    
    def get(self, *args, **kwargs):
        order=Order.objects.get(user=self.request.user,ordered=False)
        if order.billingAddress:
            context = {
                "order": order,
                # do not  display coupon form on the payment page
                "DISPLAY_COUPON_FORM": False,
            }
            
            return render(self.request, "Order/paypal_payment.html", context)
        else:
            messages.warning(
                self.request, "You have not added a billing address")
            return redirect("Order:checkout")


def paypalPaymentComplete(request):
    data=JSON.loads(request.body)
    order_id=data['orderId']
    customer=data['Customer']
    total=data['total']
    order=Order.objects.get(user=request.user,ordered=False,id=order_id)
    if total==order.get_total:
        order.ordered=True
        order.save()
    print('BODY :',data)
    return JsonResponse('payment Completed!',safe=False)
            
class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {"form": form}
        return render(self.request, "Order/request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get("ref_code")
            message = form.cleaned_data.get("message")
            email = form.cleaned_data.get("email")
            # edit the order
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # save the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("Order:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("Order:request-refund")


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("Order:checkout")


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            # upon adding coupon then
            try:
                # get the code
                code = form.cleaned_data.get("code")
                # check order
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                # assign coupon to the order
                coupon = get_coupon(self.request, code)
                order.coupon = coupon
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("Order:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("Order:checkout")
