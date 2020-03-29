from django.contrib.auth.mixins import LoginRequiredMixin #new
from django.core.exceptions import PermissionDenied #new
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView # new
from django.urls import reverse_lazy # new
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.db.models import Q
from articles.models import Article
from django.contrib.auth import get_user_model
from users.models import CustomUser 
# Create your views here.



def profiles_list_view(request):
    queryset = request.GET.get("buscar")
    custumusers = get_list_or_404(CustomUser, estado = True)
    
    if custumusers == None:
        return redirect('home')
        
    if queryset and custumusers:
        custumusers = CustomUser.objects.filter(
            Q(username__icontains = queryset) |
            Q(first_name__icontains = queryset) |
            Q(last_name__icontains = queryset) |
            Q(universidad__icontains =  queryset),
            estado = True
        ).distinct()

    return render(request, 'authors/profile_list.html', {'custumusers':custumusers})

"""
class ProfileDetailView(DetailView): # new
    model = CustomUser
    template_name = 'authors/profile_detail.html'
"""


def profileDetail(request, slug):
    customuser = get_object_or_404(CustomUser, slug = slug) 
    articles = Article.objects.filter(author = customuser, delete =False)
    
    context = {
        'customuser' : customuser,
        'articles':articles,
    }
    return render(request, 'authors/profile_detail.html', context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView): # new
    model = CustomUser
    fields = ('first_name','last_name', 'email','universidad','phone','photo','description','bio','age','facebook','linkedin','twitter','instagram','web',) #'__all__'
    template_name = 'authors/profile_edit.html'
    login_url = 'login' #new

    #Esto controla que un cualquier author NO edite los artículos que no le pertenece
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.username != self.request.user.username:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class ProfileDeleteView(LoginRequiredMixin, DeleteView): # new
    model = CustomUser
    template_name = 'authors/profile_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login' #new

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)