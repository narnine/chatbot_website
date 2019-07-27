from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Article_One(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = CloudinaryField('image', blank=True)

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








