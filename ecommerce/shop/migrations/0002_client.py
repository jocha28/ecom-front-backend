# Generated by Django 5.1.5 on 2025-01-18 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
