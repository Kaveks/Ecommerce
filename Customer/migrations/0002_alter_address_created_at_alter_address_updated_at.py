# Generated by Django 4.1.7 on 2023-02-24 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 22, 715978, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Created at",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 22, 715978, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
    ]
