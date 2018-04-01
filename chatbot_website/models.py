from django.db import models


# Create your models here.
class Article_One(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(blank=True)


class Article_Two(models.Model):
    title = models.CharField(max_length=100)
    title_first = models.CharField(max_length=100)
    text_first = models.TextField()
    image_first = models.ImageField(blank=True)
    title_second = models.CharField(max_length=100)
    text_second = models.TextField()
    image_second = models.ImageField(blank=True)
    title_third = models.CharField(max_length=100)
    text_third = models.TextField()
    image_third = models.ImageField(blank=True)

class Article_Three(models.Model):
    title = models.CharField(max_length=100)
    title_first = models.CharField(max_length=100)
    text_first = models.TextField()
    image_first = models.ImageField(blank=True)
    title_second = models.CharField(max_length=100)
    text_second = models.TextField()
    image_second = models.ImageField(blank=True)

class Article_Fourth(models.Model):
    title_first = models.CharField(max_length=100)
    text_first = models.TextField()


