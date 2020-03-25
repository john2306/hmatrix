from django.urls import path
from django.conf.urls import url
from .views import  *

urlpatterns = [
    path('',home , name='home'),
    path('datascience/', datascience_view, name = 'datascience'), #new
    path('neurociencia/', neurociencia_view, name = 'neurociencia'), #new
    path('projects/', education_view, name = 'projects'), #new
]
