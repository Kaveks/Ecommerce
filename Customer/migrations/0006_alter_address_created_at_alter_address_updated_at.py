# Generated by Django 4.1.7 on 2023-02-28 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0005_alter_address_created_at_alter_address_customer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 58, 668825, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Created at",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 58, 668825, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
    ]
