# Generated by Django 3.2.4 on 2021-08-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0022_order_egy_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product_cart',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]