# Generated by Django 4.2.2 on 2023-07-09 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Trade",
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
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trader1",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trader2",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Clothing",
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
                ("image", models.ImageField(upload_to="images")),
                ("image_data", models.BinaryField(null=True)),
                ("title", models.CharField(max_length=100)),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("Red", "Red"),
                            ("Orange", "Orange"),
                            ("Yellow", "Yellow"),
                            ("Green", "Green"),
                            ("Blue", "Blue"),
                            ("Purple", "Purple"),
                            ("Pink", "Pink"),
                            ("Brown", "Brown"),
                            ("Black", "Black"),
                            ("White", "White"),
                            ("Other", "Other"),
                        ],
                        default=("Other", "Other"),
                        max_length=100,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("XS", "XS"),
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("XL", "XL"),
                        ],
                        default=("XL", "XL"),
                        max_length=100,
                    ),
                ),
                (
                    "cType",
                    models.CharField(
                        choices=[
                            ("Shirts", "Shirts"),
                            ("Pants", "Pants"),
                            ("Sweaters", "Sweaters"),
                            ("Other", "Other"),
                        ],
                        default=("Other", "Other"),
                        max_length=100,
                    ),
                ),
                (
                    "trade",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clothing",
                        to="home.trade",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clothing",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]