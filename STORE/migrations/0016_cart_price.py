# Generated by Django 3.2.4 on 2021-08-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0015_address_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
