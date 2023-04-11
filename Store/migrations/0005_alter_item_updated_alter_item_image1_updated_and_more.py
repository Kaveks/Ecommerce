# Generated by Django 4.1.7 on 2023-04-05 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0004_alter_item_additional_info_alter_item_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 11, 16, 52, 148657, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image1",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 11, 16, 52, 148657, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image2",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 11, 16, 52, 148657, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image3",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 11, 16, 52, 148657, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image4",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 5, 11, 16, 52, 148657, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
    ]