# Generated by Django 2.0.3 on 2021-03-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_website', '0018_article_three_article_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='../static/chatbot_website/img/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
