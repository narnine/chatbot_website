from django.contrib import admin
from .models import Article_One, News
from .models import  Article_Two
from .models import Article_Three

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
admin.site.register(Article_One)
admin.site.register(Article_Two)
admin.site.register(Article_Three)
admin.site.register(News, NewsAdmin)
