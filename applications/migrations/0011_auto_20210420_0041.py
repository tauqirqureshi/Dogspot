# Generated by Django 3.1.2 on 2021-04-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_auto_20210420_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile_no',
            field=models.BigIntegerField(),
        ),
    ]
