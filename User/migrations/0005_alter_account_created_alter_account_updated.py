# Generated by Django 4.1.7 on 2023-02-28 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0004_rename_las_name_account_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 4706, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 4706, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]