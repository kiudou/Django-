from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def index(request):
    return HttpResponse("hello world!")


def detail(request, question_id):
    post = Article.objects.all()[int(question_id)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
         % (post.title, post.category, post.time, post.content))
    return HttpResponse(str)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)