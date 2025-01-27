# Generated by Django 5.1.5 on 2025-01-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_seller_cover_photo_seller_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]
