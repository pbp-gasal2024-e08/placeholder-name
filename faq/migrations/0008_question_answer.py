# Generated by Django 5.1.2 on 2024-10-27 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0007_remove_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=''),
        ),
    ]