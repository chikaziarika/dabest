from django.urls import path, include, re_path
from . import views
from .views import *
# from django.contrib.auth import views as auth_views

from rest_framework import routers
from django.conf.urls.static import static


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'joblist', views.CareerViewSet)
router.register(r'dataProject', views.ProjectViewSet)
router.register(r'dataPelamar', views.ApplicantViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('webhook', views.webhook, name='webhook'),
    path('services', views.servicesPage, name='services'),
    path('playingfield', views.playingFieldPage, name='playingfield'),
    path('SnD', views.SnDPage, name='SnD'),
    path('sitevisit', views.sitevisitPage, name='sitevisit'),
    path('servicesHD', views.servicesHDPage, name='servicesHD'),
    path('servicesWD', views.servicesWDPage, name='servicesWD'),
    path('servicesWR', views.servicesWRPage, name='servicesWR'),
    path('servicesWS', views.servicesWSPage, name='servicesWS'),
    path('servicesModal', views.servicesModalPage, name='servicesModal'),
    path('careers', views.careersPage, name='careers'),
    path('jobListing/<str:pk>', views.jobListingPage, name='jobListing'),
    path('apply/<str:pk>', views.applyPage, name="apply"),
    path('blogs', views.blogPage, name='blogs'),
    path('projects', views.projectPage, name='projects'),
    path('projectMaps', views.projectMapsPage, name='projectMaps'),
    path('teams', views.teamsPage, name='teams'),
    path('BoD', views.BoDPage, name='BoD'),
    path('about', views.aboutPage, name='about'),
    path('privacy', views.privacyPage, name='privacy'),
    path('disclaimer', views.disclaimerPage, name='disclaimer'),
    path('toc', views.tocPage, name='toc'),
    path('OTL', views.otlPage, name='OTL'),
    path('SOW', views.sowPage, name='SOW'),
    path('LOS', views.losPage, name='LOS'),
    path('culture', views.culturePage, name='culture'),
    path('dashboard', views.dashboardPage, name='dashboard'),
    path('expertise', views.expertisePage, name='expertise'),
    path('test', views.testPage, name='test'),
    path('organization', views.organizationPage, name='organization'),
    path('underconst', views.underconstPage, name='underconst'),

    path('modalWRC/', views.modalWRCPage, name='modalWRC'),
    path('modalWSU/', views.modalWSUPage, name='modalWSU'),
    path('modal/', views.modalGeneral, name='modal'),
    path('modalNested/', views.modalNestedGeneral, name='modalNested'),

    path('contact', views.contactPage, name='contact'),
    
    # path('dashboard', views.dashboard, name='dashboard'),
    path('webscrap', views.WebScrap, name="webscrap"),

    # path('register/', views.register_request, name='register'),
    # path("login", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("callback", views.callback, name="callback"),
    path('script/', views.scriptPage, name="script"),
    path('error403', views.error403Page, name="error403"),
    path('package', views.packagePage, name="package"),
    path('apply/', views.applyPage, name="apply"),
    path('profile/',views.profile,name='profile'),

    path('settings/', views.UserEditView.as_view(), name='settings'),
    path('api-auth/', include('rest_framework.urls')),
    path('sentry-debug/', trigger_error),

    path('dataPerusahaan/', views.dataPerusahaanPage, name="dataPerusahaan"),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    
    # re_path(r'^password/$', views.change_password, name='change_password'),
    path("chpass", views.change_password, name="change_password"),

] 
urlpatterns += router.urls  
