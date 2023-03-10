# Generated by Django 4.1.7 on 2023-02-27 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0003_alter_address_created_at_alter_address_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="full_name",
            field=models.CharField(help_text="required", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 27, 5, 14, 27, 964619, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Created at",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 2, 27, 5, 14, 27, 964619, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Updated at",
            ),
        ),
    ]
