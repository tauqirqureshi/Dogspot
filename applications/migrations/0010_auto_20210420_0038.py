# Generated by Django 3.1.2 on 2021-04-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_auto_20210420_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile_no',
            field=models.IntegerField(),
        ),
    ]
