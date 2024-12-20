# Generated by Django 5.1.2 on 2024-10-27 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main", "0001_initial"),
        ("myauth", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                    "quantity",
                    models.PositiveIntegerField(blank=True, default=1),
                ),
                (
                    "total_price",
                    models.PositiveIntegerField(blank=True, default=1, null=True),
                ),
                (
                    "payment",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("date", models.DateTimeField(blank=True, null=True)),
                (
                    "product",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myauth.ajeguser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("date", models.DateTimeField()),
                ("cart", models.ManyToManyField(to="checkout.cart")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myauth.ajeguser",
                    ),
                ),
            ],
        ),
    ]
