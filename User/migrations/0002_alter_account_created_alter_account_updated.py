# Generated by Django 4.1.7 on 2023-02-24 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 51, 415140, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 51, 415140, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]