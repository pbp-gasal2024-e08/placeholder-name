# Generated by Django 5.1.2 on 2024-10-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expiry_date', models.DateTimeField()),
                ('is_claimed', models.BooleanField(default=False)),
                ('is_flash_sale', models.BooleanField(default=False)),
            ],
        ),
    ]
