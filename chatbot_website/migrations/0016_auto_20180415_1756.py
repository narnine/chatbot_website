# Generated by Django 2.0.3 on 2018-04-15 11:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0015_auto_20180404_1641'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article_Fourth',
        ),
        migrations.AlterField(
            model_name='article_one',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article_three',
            name='image_first',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article_three',
            name='image_second',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
