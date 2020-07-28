# Generated by Django 2.2.12 on 2020-07-21 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('initial_amount', models.CharField(default='0', max_length=100)),
                ('total_amount', models.CharField(default='0', max_length=100)),
                ('total_amount_gained', models.CharField(default='0', max_length=100)),
                ('total_amount_spent', models.CharField(default='0', max_length=100)),
            ],
        ),
    ]