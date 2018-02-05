from django.urls import path

from . import views

urlpatterns = [
    # ex: /article/
    path('', views.index, name='index'),
    # ex: /article/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /article/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /article/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
