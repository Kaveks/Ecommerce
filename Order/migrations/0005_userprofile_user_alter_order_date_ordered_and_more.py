# Generated by Django 4.1.7 on 2023-04-06 11:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Order", "0004_remove_userprofile_user_alter_order_date_ordered_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="date_ordered",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 33, 34, 866152, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 33, 34, 866152, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 33, 34, 866152, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="refund",
            name="refund_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 33, 34, 866152, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
