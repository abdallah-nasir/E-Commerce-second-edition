# Generated by Django 3.2.4 on 2021-08-25 17:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0030_remove_blogs_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='details',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
