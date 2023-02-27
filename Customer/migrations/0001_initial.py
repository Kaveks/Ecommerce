# Generated by Django 4.1.7 on 2023-02-24 15:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Required ",
                        max_length=255,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Required ",
                        max_length=50,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "zipcode",
                    models.CharField(
                        blank=True,
                        help_text="Optional ",
                        max_length=50,
                        verbose_name="Postcode",
                    ),
                ),
                (
                    "address_line",
                    models.CharField(
                        blank=True,
                        help_text="Optional ",
                        max_length=255,
                        verbose_name="Address 1",
                    ),
                ),
                (
                    "address_line2",
                    models.CharField(
                        blank=True,
                        help_text="Optional ",
                        max_length=255,
                        verbose_name="Address2",
                    ),
                ),
                ("country", django_countries.fields.CountryField(max_length=2)),
                (
                    "town_city",
                    models.CharField(
                        help_text="Required ",
                        max_length=255,
                        verbose_name="Town/City/State",
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        choices=[("B", "Billing"), ("S", "Shipping")], max_length=1
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 2, 24, 18, 8, 5, 716919, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="Created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 2, 24, 18, 8, 5, 716919, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="Updated at",
                    ),
                ),
                ("default", models.BooleanField(default=False, verbose_name="Default")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customers",
                        to="Customer.customer",
                        verbose_name="Customer",
                    ),
                ),
            ],
            options={
                "verbose_name": " Customer Address",
                "verbose_name_plural": "Customer Addresses",
            },
        ),
    ]