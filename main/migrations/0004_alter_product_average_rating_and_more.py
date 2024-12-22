# Generated by Django 5.1.4 on 2024-12-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='review_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
