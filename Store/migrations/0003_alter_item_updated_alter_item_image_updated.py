# Generated by Django 4.1.7 on 2023-02-24 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0002_alter_item_updated_alter_item_image_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 51, 411142, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="Updated at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 24, 18, 9, 51, 411142, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
    ]
