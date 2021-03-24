from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse


# Create your models here.
class Article_One(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья тип 1'
        verbose_name_plural = 'Статья тип 1'
        ordering = ['title']


class Article_Two(models.Model):
    title = models.CharField(max_length=100)
    title_first = models.CharField(max_length=100)
    text_first = models.TextField()
    image_first = CloudinaryField('image', blank=True)
    title_second = models.CharField(max_length=100)
    text_second = models.TextField()
    image_second = CloudinaryField('image', blank=True)


class Article_Three(models.Model):
    title = models.CharField(max_length=100)
    title_first = models.CharField(max_length=100)
    text_first = models.TextField()
    image_first = CloudinaryField('image')
    title_second = models.CharField(max_length=100)
    text_second = models.TextField()
    image_second = CloudinaryField('image')
    title_third = models.CharField(max_length=100)
    text_third = models.TextField()
    image_third = CloudinaryField('image')


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновленно')
    photo = models.ImageField(blank=True, upload_to='static/chatbot_website/img/%Y/%m/%d/', verbose_name='Опубликовано')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
