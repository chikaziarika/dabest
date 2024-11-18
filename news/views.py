from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext
from main.models import *
from bs4 import BeautifulSoup
from article.models import *
from .models import *
import requests


# Create your views here.

def translate(language):
    cur_language = get_language()
    try :
        activate(language)
        text = gettext("What's problem our business is trying to solved")
    finally :
        activate(cur_language)
    return text

def news(request):
    
    trans = translate(language='id')

    news = News.objects.all()

    latest = News.objects.all()

    
    article = Article.objects.filter(artstatus='Approve')

    # educationLatest = Article.objects.filter(artstatus='Approve').order_by('-createAt')[:5]

    dataKegiatan = Kegiatan.objects.all()

    # allPosts = News.tags.all()

    # URL = "https://www.antaranews.com/warta-bumi"
    # r = requests.get(URL)
    # # soup = BeautifulSoup(r.content, "html.parser")
    # soup = BeautifulSoup(r.content, "lxml")
    # # results = soup.find_all('div',class_='card__post')
    # # print(f"{len(results):3} {URL}") 
    # # print("nihh...", soup.prettify())
    # # soup2 = BeautifulSoup(r.content, 'html')
    # # elements = soup.find_all('div', class_='card__post card__post-list card__post__transition mt-30')
    # elements = soup.find_all('div', class_='card__post card__post-list card__post__transition mt-30')
    # # print('nIH...',elements)
    
    # data = []
    # for article in elements:
    #     title = article.find('h2', class_='post_title post_title_medium').text
    #     link = article.find_all('a', href=True)
    #     img = article.find('img').get('data-src')
        
    #     # print('Nih IMAGE.......',img.get('data-src'))
    #     createAt = article.find('div', class_='card__post__author-info mb-2').text
    #     desc = article.find('p').text
    #     # print('nIH...',link)
    #     # link = article.find['href']
    #     # print('nIH...',title)
    #     data.append((title, link, createAt, desc, img))

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'posts':news,
        'latest':latest,
        'recentEdu':article,
        'dataKegiatan':dataKegiatan,
        # 'dataB':article,
        # 'allPosts':allPosts
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'news/news.html', context)

def articlePage(request, pk):
    
    trans = translate(language='id')
    
    article = News.objects.filter(id=pk)

    posts = News.objects.all()

    

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'posts':posts,
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'news/article.html', context)