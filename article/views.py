from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext
from .models import *
from main.models import *
from django.db.models import Q, Count
from .forms import CommentForm, BlogForm
from django.http import HttpResponseRedirect
from article.models import Tag as xTag


def translate(language):
    cur_language = get_language()
    try :
        activate(language)
        text = gettext("What's problem our business is trying to solved")
    finally :
        activate(cur_language)
    return text

def blogPage(request):
    
    trans = translate(language='id')

    data = Article.objects.filter(artstatus='Approve')

    issue = Issue.objects.all()
    
    dataB = Article.objects.filter(artstatus='Approve').order_by('-createAt')[:5]

    articleTags = Tag.objects.all()

    

    # for tag in tags:
    #     data = data.filter(tags__name=tag)

    result = Article.objects.filter(artstatus='Approve').filter(tags__in=articleTags).exclude(tags=0).distinct()
    
    
    # dataResult = result
    # resultList = list(result.values_list('tags', flat=True))
    print('TEST.....', result)

    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'data':data,
        'issue':issue,
        'dataB':dataB,
        'articleTags':articleTags,
        'articleTest':result,
        

    }

    return render(request, 'article/blogs.html', context)


def activityPage(request, pk):
    
    trans = translate(language='id')

    data = Kegiatan.objects.filter(ids=pk)

    other = Kegiatan.objects.all();

   
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'data':data,
        'other':other,
        

    }

    return render(request, 'main/activity.html', context)

def readMainPage(request, pk):
    
    trans = translate(language='id')
    
    article = Article.objects.filter(id=pk)

    other = Article.objects.filter(artstatus='Approve')

    Tags = xTag.objects.all()
    print('apa ini...',)

    post = Article.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                article=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(article=post)

    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'form':CommentForm(),
        "comments": comments,
        'post':post,
        'other':other,
        'Tags':Tags,
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/mainarticle.html', context)


def issuePage(request, pk):
    
    trans = translate(language='id')
    
    article = Issue.objects.filter(id=pk)

    # issueTags = Tag.objects.filter(Tag=Issue)

    # results = Article.objects.filter(artstatus='Approve').exclude(tags=0).distinct()
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/issue.html', context)

def issueMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Issue')

    data = Article.objects.filter(tags__nameTag='Issue').filter(artstatus='Approve')
    
    print('Waw......', Tags)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/issuepage.html', context)


def factMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Fact')

    data = Article.objects.filter(tags__nameTag='Fact').filter(artstatus='Approve')
    
    # print('Waw......', Tags)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/factpage.html', context)

def buildingMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Building')

    data = Article.objects.filter(tags__nameTag='Building').filter(artstatus='Approve')
    
    # print('Waw......', Tags)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/Buildingpage.html', context)

def managementMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Management')

    data = Article.objects.filter(tags__nameTag='Management').filter(artstatus='Approve')
    
    # print('Waw......', Tags)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/managementpage.html', context)

def communityMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Community')

    data = Article.objects.filter(tags__nameTag='Community').filter(artstatus='Approve')
    
    # print('Waw......', Tags)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/communitypage.html', context)

def tipsMainPage(request):
    
    trans = translate(language='id')
    
    article = Issue.objects.all()

    Tags = xTag.objects.all().exclude(nameTag='Tips')

    data = Article.objects.filter(tags__nameTag='Tips').filter(artstatus='Approve')
    
    print('Waw......', data)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'data':data,
        'Tags':Tags,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/tipspage.html', context)

def userarticlePage(request):
    
    trans = translate(language='id')
    article = Article.objects.filter(artstatus='Approve')
    Issue = Article.objects.filter(tags__nameTag='Issue').filter(artstatus='Approve')
    Fact = Article.objects.filter(tags__nameTag='Fact').filter(artstatus='Approve')
    Building = Article.objects.filter(tags__nameTag='Building').filter(artstatus='Approve')
    Management = Article.objects.filter(tags__nameTag='Management').filter(artstatus='Approve')
    Community = Article.objects.filter(tags__nameTag='Community').filter(artstatus='Approve')
    Tips = Article.objects.filter(tags__nameTag='Tips').filter(artstatus='Approve')

    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':Issue,
        'article2':Fact,
        'allArticle':article,
        'article3':Building,
        'article4':Management,
        'article5':Community,
        'article6':Tips,
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/userarticle.html', context)

def DetailArticlePage(request,pk):
    
    trans = translate(language='id')
    
    article = Article.objects.filter(id=pk)

    post = Article.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                article=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(article=post)
    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'article':article,
        'form':CommentForm(),
        "comments": comments,
        'post':post
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/detailarticle.html', context)


def newPost(request):
    
    trans = translate(language='id')
    form = BlogForm()
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/article")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()

    
    context = {
        
        'trans':trans,
        "available_languages": ["en", "id" ],
        'form':form
        
        
        # 'LANGUAGES':['en','id']

    }

    return render(request, 'article/newpost.html', context)