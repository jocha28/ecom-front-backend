# Generated by Django 5.1.5 on 2025-01-19 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_product_photo_prducts_product_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="photo_prducts",
        ),
        migrations.RemoveField(
            model_name="product",
            name="video",
        ),
    ]
