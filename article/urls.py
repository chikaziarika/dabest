from django.urls import path, include
from . import views
from .views import *

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('article', views.blogPage, name='article'),
    path('activity/<str:pk>', views.activityPage, name='activity'),
    path('read/<str:pk>', views.readMainPage, name='read' ),
    path('issue/<str:pk>', views.issuePage, name='issue' ),
    path('userarticle', views.userarticlePage, name='userarticle'),
    path('detailarticle/<str:pk>', views.DetailArticlePage, name='detailarticle'),
    path('Issuepage', views.issueMainPage, name='Issuepage' ),
    path('Factpage', views.factMainPage, name='Factpage' ),
    path('Buildingpage', views.buildingMainPage, name='Buildingpage' ),
    path('Managementpage', views.managementMainPage, name='Managementpage' ),
    path('Communitypage', views.communityMainPage, name='Communitypage' ),
    path('Tipspage', views.tipsMainPage, name='Tipspage' ),
    path('newpost', views.newPost, name='newpost' ),
    # path('issuepage/<str:pk', views.issueMainPage, name='issuepage' ),
] 
urlpatterns 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)