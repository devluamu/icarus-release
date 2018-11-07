# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import NoticePost

def index(request):
    template = loader.get_template('web/anime-index.html')
    return render(request, 'web/anime-index.html')

def notice(request):
    posts = NoticePost.objects.get_queryset().order_by('-id')
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'web/notice.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(NoticePost, pk=post_id)
    
    return render(request, 'web/notice-detail.html', {'post': post}) 

def term(request):
    return render(request, 'web/terms.html')
    
# Create your views here.
