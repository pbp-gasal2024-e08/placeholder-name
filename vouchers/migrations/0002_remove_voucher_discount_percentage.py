# Generated by Django 5.1.2 on 2024-10-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='discount_percentage',
        ),
    ]
