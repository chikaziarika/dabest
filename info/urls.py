from django.urls import path, include
from . import views
from .views import *

# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('info', views.info, name='info'),
    path('infoapi', views.infoApi, name='infoapi'),
    # path('article/<str:pk>', views.articlePage, name='article'),
 


] 
urlpatterns 