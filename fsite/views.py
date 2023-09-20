from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


blog = [  {'title_': 'Читать', 'url_name_': 'read_blog'},
          {'title_': 'Читать', 'url_name_': 'read_blog'},
          {'title_': 'Читать', 'url_name_': 'read_blog'},
            ]


menu = [ {'title': 'Главная', 'url_name': ''},
         {'title': 'Обо мне', 'url_name': 'about'},
         {'title': 'Тренинги', 'url_name': 'treningi'},
         {'title': 'Блоги', 'url_name': 'blog'},

]






def index(request):
    posts = Company.objects.all()
    pests = Trenings.objects.all()
    socials = Socials.objects.all()
    blogs = Blogs.objects.all()
    context = {
        'posts': posts,
        'pests': pests,
        'socials': socials,
        'menu': menu,
        'blog': blog,
        'blogs': blogs,
        'title': 'Главная страница',
        'title_companys': 'Компании',
        'title_treningi':'Тренинги',
        'title_blogs': 'Блоги',
        'cat_selected': 0,
    }

    return render(request, 'fsite/base.html', context=context)

def about(request):
    socials = Socials.objects.all()
    posts = Company.objects.all()
    context = {
        'title_companys': 'Компании',
        'menu': menu,
        'posts': posts,
        'title': 'Обо мне',
        'socials': socials,
    }
    return render(request, 'fsite/about.html', context=context)

def treningi(request):
    socials = Socials.objects.all()
    pests = Trenings.objects.all()
    context = {
        'pests': pests,
        'socials': socials,
        'menu': menu,
        'title': 'Тренинги',
    }
    return render(request, 'fsite/treningi.html', context=context)

def blog(request):
    socials = Socials.objects.all()
    blogs = Blogs.objects.all()

    context = {
        'menu': menu,
        'title_blogs': 'Блоги',
        'blog': blog,
        'blogs': blogs,
        'socials': socials,
        'title': 'Блог',
    }
    return render(request, 'fsite/blog.html', context=context)


def show_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    blogs = Blogs.objects.all()

    context = {
        'menu': menu,
        'title_blogs': 'Блоги',
        'blogs': blogs,
        'blog': blog,
        'title': blog.title,
    }
    return render(request, 'fsite/show_blog.html', context=context)

