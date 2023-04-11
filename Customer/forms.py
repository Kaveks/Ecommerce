from django import forms
from Customer.models import Address


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name","last_name", "email", "phone", "country",
                  "town_city", "address", "address2", "zipcode","address_type",]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "First Name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Last Name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "email"})
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Phone"})
        self.fields["country"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "country"})

        self.fields["address"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address"}
        )
        self.fields["address2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address2"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "city"}
        )
        self.fields["zipcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "zipcode"}
        )
        self.fields["address_type"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "zipcode"}
        )