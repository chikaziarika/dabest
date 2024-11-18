from django.urls import path, include
from . import views
from .views import *

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('news', views.news, name='news'),
    path('article/<str:pk>', views.articlePage, name='article' ),


] 
urlpatterns 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)