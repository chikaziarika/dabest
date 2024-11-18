from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext
from main.models import *
import requests
import json
from django.http import HttpResponse

# Create your views here.

def translate(language):
    cur_language = get_language()
    try :
        activate(language)
        text = gettext("What's problem our business is trying to solved")
    finally :
        activate(cur_language)
    return text

def info(request):
    # trans =  _("What's problem our business is trying to solved")
    trans = translate(language='id')

    # news = News.objects.all()

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        # 'posts':news
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'info/info.html', context)

def infoApi(request):
    # trans =  _("What's problem our business is trying to solved")
    # trans = translate(language='id')

    # response = requests.get(f'https://newsapi.org/v2/top-headlines?country=id&apiKey=f17be268a41548749a8fba42c9c68737').json()
    # author = response.get('status')
    # title = response.get('title')
    # # news = News.objects.all()

    # context = {
        
    #     'trans':trans,
    #     "available_languages": ["en", "id" ],
    #     # 'posts':news
    #     # 'LANGUAGES':['en','id']
    #     'response':response,
    #     'author':author,
    #     'title':title,

    # }

    # return render(request, 'info/infoapi.html', context)

    your_list = requests.get(f'https://berita-indo-api-next.vercel.app/api/antara-news/warta-bumi').json()
    your_list_as_json = json.dumps(your_list)
    return HttpResponse(your_list_as_json)