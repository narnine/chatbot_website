# Generated by Django 2.0.3 on 2018-03-31 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0008_article_three'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Fourth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_first', models.CharField(max_length=100)),
                ('text_first', models.TextField()),
                ('image_first', models.ImageField(upload_to='')),
                ('title_second', models.CharField(max_length=100)),
                ('text_second', models.TextField()),
                ('image_second', models.ImageField(upload_to='')),
                ('title_third', models.CharField(max_length=100)),
                ('text_third', models.TextField()),
                ('image_third', models.ImageField(upload_to='')),
                ('title_fourth', models.CharField(max_length=100)),
                ('text_fourth', models.TextField()),
                ('image_fourth', models.ImageField(upload_to='')),
            ],
        ),
    ]
