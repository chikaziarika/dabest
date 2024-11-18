from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_user, admin_only
from .forms import *
from multiprocessing import context
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .serializers import *
from itertools import chain
import json
from authlib.integrations.django_client import OAuth
from article.models import *

from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout as django_logout
from django.conf import settings
from .forms import ModelFormWithFileField
from django.utils.translation import gettext as _ 
from django.utils.translation import get_language, activate, gettext
from multiprocessing import context
import json
from django.template.loader import render_to_string
from .meta_gen import meta_keywords
from django.core.files.storage import FileSystemStorage
import requests
from bs4 import BeautifulSoup
from htmlmin.decorators import minified_response
import os
from itertools import chain
from django.contrib.admin.models import LogEntry
from django_filters.rest_framework import DjangoFilterBackend
this_template = "main/main.html"

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.body)
        return HttpResponse("Webhook received!")

def tabs(request):
    context = {
        'items': Item.objects.all()
    }
    return render(this_template, { 'title' : "Page Name", 'keys' : meta_keywords(render_to_string(this_template)) }, context)

# oauth = OAuth()

# oauth.register(
#     "auth0",
#     client_id=settings.AUTH0_CLIENT_ID,
#     client_secret=settings.AUTH0_CLIENT_SECRET,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
# )

# def login(request):
#     return oauth.auth0.authorize_redirect(
#         request, request.build_absolute_uri(reverse("callback"))
#     )


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tahun','unitImpact','ktPekerjaan']

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    



class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = UploadApplicant.objects.all()
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    

@api_view(['GET'])
def job_list(request):
    snippets = Career.objects.all()
    serializer = CareerSerializer(snippets, many=True)
    return Response(serializer.data)



def translate(language):
    cur_language = get_language()
    try :
        activate(language)
        text = gettext("What's problem our business is trying to solved")
    finally :
        activate(cur_language)
    return text

def is_valid_queryparam(param):
    return param != '' and param is not None

@minified_response
def home(request):
    # trans =  _("What's problem our business is trying to solved")
    trans = translate(language='id')
    
    issue = Issue.objects.all()

    Years = Project.objects.all().values_list('tahun', flat=True).distinct().order_by('tahun').exclude(tahun__isnull=True)
    year_exact_query = request.GET.get('test')
    
    if is_valid_queryparam(year_exact_query) :
        Years = Years.filter(tahun__icontain=year_exact_query)

    
    Impact = Project.objects.all().values_list('impact', flat=True).values_list('unitImpact', flat=True).distinct().exclude(unitImpact__isnull=True)
    # print('A..........', Impact)
    
    Kategori = Project.objects.all().values_list('ktPekerjaan', flat=True).distinct().exclude(ktPekerjaan__isnull=True)

    # numImpact = Impact = Project.objects.all().values_list('impact', flat=True).distinct().order_by('impact').exclude(impact__isnull=True)
    
    # print('nih..', Kategori)

    dataB = Article.objects.filter(artstatus='Approve').order_by('-createAt')[:5]
    
    if request.method == 'POST' and 'btnWA' in request.POST:
        
        packages = request.POST['package'];
        projectInput = request.POST['project'];
        servicepackages = request.POST['servicepackages'];
        namaPerusahaan = request.POST['companyInputz']

        import pywhatkit

        try:
        
            # sending message to receiver
            # using pywhatkit
            pywhatkit.sendwhatmsg_instantly(phone_no="<+6281280862017>",
                                            message="Hallo Ka Admin DABEST \
                                            \nSaya dari "+namaPerusahaan+"\
                                            \nIngin bertanya mengenai\
                                            \n \
                                            \n Pekerjaan :  \
                                            \n "+packages+"  \
                                            \n Detail Pekerjaan : \
                                            \n "+projectInput+"  \
                                            \n Services : \
                                            \n "+servicepackages+"  \
                                            \n  \
                                            \n  \
                                            \n Terima Kasih" , 
                                            tab_close=True)
            print("Successfully Sent!")
        
        except:
        
            # handling exception 
            # and printing error message
            print("An Unexpected Error!") 
            print(request.build_absolute_uri())
        # return user to required page
        return HttpResponseRedirect(reverse('home'))


    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'issue':issue,
        'dataB':dataB,
        'Years':Years,
        'Impact':Impact,
        'Kategori':Kategori,
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/base.html', context)



# @unauthenticated_user 
def register_request(request):
    form = CreateUserForm()
    if request.method == "POST" :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Akun Berhasil Dibuat untuk ' + user)
            return redirect('login')

    context={'form':form}
    return render(request, 'registration/register.html', context)

# def loginPage(request):
        
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password = request.POST.get('password')
               

# 			user = authenticate(request, username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')

# 			else:
# 				messages.info(request, 'Username OR password is incorrect, Please Try Again')

# 		context = {}
        
# 		return render(request, 'registration/login.html', context)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user     

# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     request.session["user"] = token
#     return redirect(request.build_absolute_uri(reverse("home")))

# def logout(request):
#     request.session.clear()

#     return redirect(
#         f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": request.build_absolute_uri(reverse("index")),
#                 "client_id": settings.AUTH0_CLIENT_ID,
#             },
#             quote_via=quote_plus,
#         ),
#     )

# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={
#             "session": request.session.get("user"),
#             "pretty": json.dumps(request.session.get("user"), indent=4),
#         },
#     )



@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8080' # this can be current domain
    # return_to = '*.google.com'
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

# def dashboard(request):

#     log = LogEntry.objects.select_related().all().order_by("id")

#     context  = {
#         'log':log,
#     }
#     # query_results = EmailTemplate.objects.all()
#     return request('main/dashboard.html', context)

# @login_required(login_url='error403')
def WebScrap(request):
    URL = "https://www.antaranews.com/warta-bumi"
    r = requests.get(URL)
    # soup = BeautifulSoup(r.content, "html.parser")
    soup = BeautifulSoup(r.content, "lxml")
    # results = soup.find_all('div',class_='card__post')
    # print(f"{len(results):3} {URL}") 
    # print("nihh...", soup.prettify())
    # soup2 = BeautifulSoup(r.content, 'html')
    # elements = soup.find_all('div', class_='card__post card__post-list card__post__transition mt-30')
    elements = soup.find_all('div', class_='card__post card__post-list card__post__transition mt-30')
    # print('nIH...',elements)
    
    data = []
    for article in elements:
        title = article.find('h2', class_='post_title post_title_medium').text
        link = article.find_all('a', href=True)
        img = article.find('img').get('data-src')
        
        # print('Nih IMAGE.......',img.get('data-src'))
        createAt = article.find('div', class_='card__post__author-info mb-2').text
        desc = article.find('p').text
        # print('nIH...',link)
        # link = article.find['href']
        # print('nIH...',title)
        data.append((title, link, createAt, desc, img))

    # for title, link, createAt , desc, img in data:
    #     print(f"{title:70}   {link} {createAt} {desc} {img}")
    # dataTC = []
    # for data in elements:
        # title = data.find('a')
        # print('Nih ......', xTitle.text.strip())
        # if xTitle:
        #     dataTC.append(xTitle.text.strip())
        #     print('WAW....',dataTC)
        
        
        # print(dataTC)
    # nextSib = element.findNext('p')
    # print(element.decompose())
    # for x in element:      
    # xTitle = []
    # xSubs = []
    # xDesc = []
    # for data in results:
    #     title = data.find('h2', class_="post_title post_title_medium")
    #     subtitle = data.find('h2', class_="media__subtitle")
    #     # desc = data.find('p', class_='card__post__content')
    #     if title:
    #         xTitle.append(title.text.strip())
    #     if subtitle:
    #         xSubs.append(subtitle.text.strip())
    #     # if desc:
    #     #     xDesc.append(desc.text.strip())    
    
    # datacombine = list(chain(xTitle,xSubs))
    # print('NAH..................', xTitle)
    # datacombine.append(xTitle,teks)
    # print('waw...',datacombine)


    context = {
        # 'results':results,
        'data':data,
        # 'title':title,
        # 'link':link,
        # 'xSubs':xSubs,
        # 'teks':dataTC,
        # 'listData': datacombine,
        # 'descShow':descShow,
        # 'xData':xData

    }


    return render(request, "main/webscrap.html", context)
    # return render(request, 'main/webscrap.html', {'news':news})

# def logoutUser(request):
# 	logout(request)
# 	return redirect('/')


def servicesPage(request):
    
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/services.html', context)



def playingFieldPage(request):
    
    return render(request, 'main/playingfield.html')

def SnDPage(request):
    
    return render(request, 'main/SnD.html')

def sitevisitPage(request):
    
    return render(request, 'main/sitevisit.html')


def servicesHDPage(request):
    
    return render(request, 'main/servicesHD.html')

def servicesWDPage(request):
    
    return render(request, 'main/servicesWD.html')

def servicesWRPage(request):
    
    return render(request, 'main/servicesWR.html')

def servicesWSPage(request):
    
    return render(request, 'main/servicesWS.html')


def servicesModalPage(request):
    
    return render(request, 'main/servicesModal.html')

# @login_required(login_url='error403')
def careersPage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/careers.html', context)

def packagePage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/package.html', context)


# @login_required(login_url='error403')
def jobListingPage(request, pk):
    trans = translate(language='id')

    # dept = request.GET.get('JobPos')
    # print('INI....',dept)
    # queryset2 = Career.objects.filter(department='Project')
    
    # print([p.position for p in queryset2])
    # data = Career.objects.all().filter(**DepartementList)
    

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']
        

    }
    queryset = Career.objects.get(id=pk)
    serialier = CareerSerializer(queryset, many=False)
    
    return render(request, 'main/jobListing.html', context)

def applyPage(request, pk):
    queryset = Career.objects.get(id=pk)
    serialier = CareerSerializer(queryset, many=False)
    

    # if request.method == 'POST':
    #     uploaded_file = request.FILES['document']
    #     fs = FileSystemStorage()
    #     name = fs.save(uploaded_file.name, uploaded_file)
    form = DocumentForm()
    form_2 = InputApplicantForm()
    if request.method == 'POST' and 'btnSubmit_1' in request.POST:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            Job_def = request.POST.get('jobPosition')
            print('ini files...',Job_def)  
             
            form.save()
            # handle_uploaded_file(request.FILES["file"])
            return render(request, 'main/careers.html', {'Job_def':Job_def})
    else:
        form = DocumentForm()

    if request.method == 'POST' and 'btnSubmit_2' in request.POST:
        form_2 = InputApplicantForm(request.POST)
        if form_2.is_valid():
            print('ini files...',form_2)  
            form_2.save()
            return render(request, 'main/careers.html')
        
    else:
        form_2 = InputApplicantForm()

    context  = {
        'form':form,
        'form_2':form_2
    }
    return render(request, 'main/apply.html', context)
    

def simple_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILS['document']
        print(uploaded_file.name)

    return render(request, 'main/apply.html')



# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })

def blogPage(request):
    
    return render(request, 'main/blogs.html')

@login_required(login_url='error403')
def projectPage(request):
    
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/projects.html', context)


# @login_required(login_url='error403')
def projectMapsPage(request):
    
    return render(request, 'main/projectMaps.html')

def contactPage(request):
    
    return render(request, 'main/contact.html')

def testPage(request):
    
    return render(request, 'main/test.html')

def teamsPage(request):
    
    return render(request, 'main/teams.html')

def BoDPage(request):
    
    return render(request, 'main/BoD.html')

def aboutPage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/about.html', context)

def privacyPage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/privacy.html', context)

def disclaimerPage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/disclaimer.html', context)

def tocPage(request):
    trans = translate(language='id')

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'main/toc.html', context)


def otlPage(request):
    
    return render(request, 'main/OTL.html')

def sowPage(request):
    
    return render(request, 'main/SOW.html')

def losPage(request):
    
    return render(request, 'main/LOS.html')


def culturePage(request):
    
    return render(request, 'main/culture.html')

def expertisePage(request):
    
    return render(request, 'main/expertise.html')

def modalGeneral(request):
    
    return render(request, 'main/modal.html')

def modalNestedGeneral(request):
    
    return render(request, 'main/modalNested.html')

def modalWRCPage(request):
    
    return render(request, 'modal/modalWRC.html')

def modalWSUPage(request):
    
    return render(request, 'modal/modalWSU.html')

def organizationPage(request):
    
    return render(request, 'main/organization.html')


def scriptPage(request):
    
    return render(request, 'main/script.html')

def dataPerusahaanPage(request):
    
    return render(request, 'perusahaan/dataPerusahaan.html')


def underconstPage(request):
    
    return render(request, 'main/underconst.html')


def error403Page(request):
    
    return render(request, 'main/error403.html')


def dashboardPage(request):
    log = LogEntry.objects.select_related().all().order_by("id")

    context  = {
        'log':log,
    }
    return render(request, 'main/dashboard.html', context)

# def applyPage(request):
    
#     return render(request, 'main/apply.html')


# def upload_file(request):
#     if request.method == "POST":
#         form = ModelFormWithFileField(request.POST, request.FILES['uploadFile'])
#         if form.is_valid():
#             # file is saved
#             form.save()
#             print('ini filesnya...')
#             return HttpResponseRedirect("/")
#     else:
#         form = ModelFormWithFileField()
#         print('ini filesnya...')
#     return render(request, "apply.html", {"form": form})


def profile(request):
    user=request.user

    auth0_user=user.social_auth.get(provider='auth0')

    user_data={
        'user_id':auth0_user.uid,
        'name':user.first_name,
        'picture':auth0_user.extra_data['picture']
    }

    context={
        'user_data':json.dumps(user_data,indent=4),
        'auth0_user':auth0_user
    }


    return render(request,'main/userProfile.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html', {
        'form': form
    })

