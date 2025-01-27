# Generated by Django 5.1.5 on 2025-01-18 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_client_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friendship",
            name="client_name",
        ),
        migrations.AddField(
            model_name="friendship",
            name="client",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="friendships",
                to="shop.client",
            ),
            preserve_default=False,
        ),
    ]
