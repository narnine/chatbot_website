from django.contrib import admin
from .models import  Article_One
from .models import  Article_Two
from .models import Article_Three
from .models import Article_Fourth

# Register your models here.
admin.site.register(Article_One)
admin.site.register(Article_Two)
admin.site.register(Article_Three)
admin.site.register(Article_Fourth)
