# Generated by Django 5.1.2 on 2024-10-26 18:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AjegUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('traveller', 'Traveller'), ('merchant', 'Merchant')], max_length=10)),
                ('ajeg_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ajeg_user', to=settings.AUTH_USER_MODEL)),
                ('store', models.ManyToManyField(blank=True, to='main.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreUserRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userstore', to='main.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userstore', to='myauth.ajeguser')),
            ],
        ),
    ]
