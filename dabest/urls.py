"""
URL configuration for dabest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include,  re_path

from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf.urls import include, i18n
from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('', include('info.urls')),
    path('', include('article.urls')),
    # path('instagram/', include('instagram_profile.urls')), 
    path(_('workshop/'), admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # path('', include('social_django.urls')),
    path("django-check-seo/", include("django_check_seo.urls")),
    path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
    path('accounts/', include('allauth.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n.i18n_patterns    (
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('', include('info.urls')),
    path('', include('article.urls')),
    # path('instagram/', include('instagram_profile.urls')), 
    path(_('workshop/'), admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # path('', include('social_django.urls')),
    path("django-check-seo/", include("django_check_seo.urls")),
    path("i18n/", include("django.conf.urls.i18n"), name="set_language"),
    path('accounts/', include('allauth.urls')),
    # prefix_default_language=False
    
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = _('DABEST Index')
admin.site.site_header = _('DABEST Admin')
admin.site.site_title = _('DABEST ADMIN Management')

