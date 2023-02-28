# Generated by Django 4.1.7 on 2023-02-28 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Store", "0007_alter_item_updated_alter_item_image1_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 34689, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
        migrations.AlterField(
            model_name="item_image1",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 7, 30, 52, 36688, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 7, 30, 52, 37687, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 7, 30, 52, 38686, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 7, 30, 52, 39686, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
    ]
