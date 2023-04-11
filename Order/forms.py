from typing_extensions import Required
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (("S", "Stripe"), ("P", "PayPal"),("M","Mpesa"))


class CheckoutForm(forms.Form):
    """shipping address"""
    shipping_firstname = forms.CharField( required=False,
    )
    shipping_lastname = forms.CharField( required=False,
    )
    shipping_email = forms.EmailField(
        required=False
    )
    shipping_phone = forms.CharField(
        required=False)
    shipping_address1 = forms.CharField(
        required=False,
    )
    shipping_address2 = forms.CharField(
        required=False,
    )
    shipping_country = CountryField(
        blank_label="(select country)",
    ).formfield(
        required=False,
        widget=CountrySelectWidget(
            attrs={
                "class": "custom-select d-block w-100",
            }
        ),
    )

    shipping_town = forms.CharField(
        required=False,
    )
    shipping_zipcode = forms.CharField(
        required=False,
    )

    """ billing address"""
    billing_firstname = forms.CharField(
        required=False,
    )
    billing_lastname = forms.CharField(
        required=False,
    )
    billing_email = forms.EmailField(
        required=False
    )
    billing_phone = forms.CharField(
        required=False)
    billing_address1 = forms.CharField(
        required=False,
    )
    billing_address2 = forms.CharField(
        required=False,
    )
    billing_country = CountryField(
        blank_label="(select country)",
    ).formfield(
        required=False,
        widget=CountrySelectWidget(
            attrs={
                "class": "custom-select d-block w-100",
            }
        ),
    )
    billing_town = forms.CharField(
        required=False,
    )
    billing_zipcode = forms.CharField(
        required=False,
    )
    same_billing_address = forms.BooleanField(
        required=False,
    )
    use_default_shipping_address = forms.BooleanField(
        required=False,
    )
    use_default_billing_address = forms.BooleanField(
        required=False,
    )
    set_default_billing_address = forms.BooleanField(
        required=False,
    )
    set_default_shipping_address = forms.BooleanField(
        required=False,
    )

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES
    )


class CouponForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Promo code",
                "aria-label": "Recipient's username",
                "aria-describedby": "basic-addon2",
            }
        )
    )


class RefundForm(forms.Form):
    ref_code = forms.CharField(
        label='ref code', min_length=4, max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'ref code', 'id': 'form-ref_code'}))
    message = forms.CharField(label='text', max_length=300,widget=forms.Textarea(attrs={"rows": 4,'class': 'form-control mb-3', 'placeholder': 'text', 'id': 'form-text'}))
    email = forms.EmailField(
        label=' email', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email'}))
   
        


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
