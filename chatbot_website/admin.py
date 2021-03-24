from django.contrib import admin
from .models import Article_One,Article_Two, Article_Three, News, Category

class Article_OneAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_display_links = ('title',)
    search_fields = ('title', 'text')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(Article_One, Article_OneAdmin)
admin.site.register(Article_Two)
admin.site.register(Article_Three)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)