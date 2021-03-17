from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'begin', views.begin, name='begin'),
    path(r'ourtime', views.ourtime, name='ourtime'),
    path(r'future', views.future, name='future'),
    path(r'simple', views.simple, name='simple'),
    path(r'hard', views.hard, name='hard'),
    path(r'example', views.example, name='example'),
    path(r'blog', views.blog, name='blog'),
path(r'category/<int:category_id>/', views.get_category, name='category')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
