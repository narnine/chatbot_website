# Generated by Django 2.0.3 on 2018-04-16 13:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0017_auto_20180416_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Three',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_first', models.CharField(max_length=100)),
                ('text_first', models.TextField()),
                ('image_first', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title_second', models.CharField(max_length=100)),
                ('text_second', models.TextField()),
                ('image_second', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title_third', models.CharField(max_length=100)),
                ('text_third', models.TextField()),
                ('image_third', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Two',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_first', models.CharField(max_length=100)),
                ('text_first', models.TextField()),
                ('image_first', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('title_second', models.CharField(max_length=100)),
                ('text_second', models.TextField()),
                ('image_second', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
            ],
        ),
    ]
