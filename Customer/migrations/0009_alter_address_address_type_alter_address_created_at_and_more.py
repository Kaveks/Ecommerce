# Generated by Django 4.1.7 on 2023-04-06 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0008_alter_address_created_at_alter_address_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="address_type",
            field=models.CharField(
                choices=[("Billing", "Billing"), ("Shipping", "Shipping")], max_length=8
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 16, 16, 16, 159359, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Created at",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 16, 16, 16, 159359, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
    ]
