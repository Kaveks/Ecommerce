# Generated by Django 4.1.7 on 2023-02-28 05:56

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Store", "0008_alter_item_updated_alter_item_image1_updated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 8, 56, 14, 857813, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="users_wishlist",
            field=models.ManyToManyField(
                blank=True, related_name="user_wishlist", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="item_image1",
            name="updated",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 28, 8, 56, 14, 858813, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 8, 56, 14, 859812, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 8, 56, 14, 859812, tzinfo=datetime.timezone.utc
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
                    2023, 2, 28, 8, 56, 14, 860812, tzinfo=datetime.timezone.utc
                ),
                editable=False,
                verbose_name="created at",
            ),
        ),
    ]
