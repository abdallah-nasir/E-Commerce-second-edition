# Generated by Django 3.2.4 on 2021-08-02 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0013_remove_product_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
