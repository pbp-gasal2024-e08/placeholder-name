# Generated by Django 4.2.16 on 2024-10-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]