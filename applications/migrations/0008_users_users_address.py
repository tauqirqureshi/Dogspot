# Generated by Django 3.1.2 on 2021-04-19 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0007_auto_20210412_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='users_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]