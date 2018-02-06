from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    # ex: /article/
    path('', views.index, name='index'),
    # ex: /article/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /article/archives/
    path('archives/', views.archives, name='archives'),
    # ex: /article/search_tag/
    path('tag/<str:post_tag>/', views.tag, name='tag'),
]
