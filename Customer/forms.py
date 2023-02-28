from django import forms
from Customer.models import Address


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "email", "phone", "country",
                  "town_city", "address_line", "address_line2", "zipcode",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "email"})
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Phone"})
        self.fields["country"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "country"})

        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address1"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address2"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "city"}
        )
        self.fields["zipcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "zipcode"}
        )
