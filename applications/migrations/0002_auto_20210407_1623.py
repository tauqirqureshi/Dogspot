# Generated by Django 3.1.2 on 2021-04-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
