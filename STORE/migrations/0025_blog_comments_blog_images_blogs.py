# Generated by Django 3.2.4 on 2021-08-23 10:44

import STORE.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('STORE', '0024_auto_20210822_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('blog_num', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_num', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=STORE.models.blog_image_upload)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hashtag', models.CharField(max_length=150)),
                ('comments', models.ManyToManyField(to='STORE.Blog_Comments')),
                ('image', models.ManyToManyField(to='STORE.Blog_Images')),
            ],
        ),
    ]