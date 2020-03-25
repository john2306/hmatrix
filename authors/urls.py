from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('', profiles_list_view, name='profile_list'),

    path('profile/<slug:slug>/edit/',
        ProfileUpdateView.as_view(), name='profile_edit'), # new

    path('profile/<slug:slug>/',
        profileDetail, name='profile_detail'), # new

    path('profile/<int:pk>/delete/',
        ProfileDeleteView.as_view(), name='profile_delete'), # new


]
