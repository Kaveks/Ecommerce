# Generated by Django 4.1.7 on 2023-02-28 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Order", "0003_alter_order_date_ordered_alter_orderitem_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 41685, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 40686, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 43684, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="refund",
            name="refund_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 44683, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
