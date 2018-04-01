from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('begin/$', views.begin, name='begin'),
    path('ourtime/$', views.ourtime, name='ourtime')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
