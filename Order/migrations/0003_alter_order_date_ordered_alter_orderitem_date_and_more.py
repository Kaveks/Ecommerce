# Generated by Django 4.1.7 on 2023-02-28 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Order", "0002_alter_order_date_ordered_alter_orderitem_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 33, 596831, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 33, 596831, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 33, 597831, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="refund",
            name="refund_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 6, 48, 33, 598830, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
