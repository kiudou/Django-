from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
# Create your views here.


def index(request):
    return HttpResponse("hello world")


def home(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, question_id):
    try:
        post = Article.objects.get(id=str(question_id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def tag(request, post_tag):
    try:
        post_list = Article.objects.filter(category__iexact=str(post_tag)) #category__iexact=str(post_tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})
    else:
        return redirect('/')
