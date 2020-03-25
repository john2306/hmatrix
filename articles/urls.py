from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('new/', ArticleCreateView.as_view(), name='article_new'), #new
    path('<slug:slug>/',ArticleDetailView.as_view(), name='article_detail'), # new
    path('<slug:slug>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<slug:slug>/delete/',article_delete , name='article_delete'), # new
]