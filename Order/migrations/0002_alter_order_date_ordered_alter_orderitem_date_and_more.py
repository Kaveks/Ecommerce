# Generated by Django 4.1.7 on 2023-04-05 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Order", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 8, 38, 1, 124976, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 8, 38, 1, 124976, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 8, 38, 1, 132975, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="refund",
            name="refund_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 8, 38, 1, 132975, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
