# Generated by Django 4.1.7 on 2023-04-06 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0004_alter_account_created_alter_account_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 30, 9, 887042, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 6, 14, 30, 9, 887042, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
