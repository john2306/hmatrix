from django.contrib.auth.mixins import LoginRequiredMixin #new
from django.core.exceptions import PermissionDenied #new
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.paginator  import Paginator
from django.core.mail import send_mail


from .models import Article
# Create your views here.

class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(status = True, delete = False)
    template_name = 'home.html' 

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article/article_new.html'
    fields = ('title', 'image','description','category', 'body','status',)      #'__all__'
    login_url = 'login' #new
    
    #el campo author se llena de forma automática cuando el usuario se logea.
    def form_valid(self, form):
        form.instance.author = self.request.user
        #Le notificas que creó un artículo.
        send_mail(
            'Creaste un nuevo artículo', 
            'Es genial saber que sigues aportando a la comunidad \ncon tu investigación, conocimiento y buenas propuestas',
            'do-not-reply@example.com',
            [self.request.user.email]
            )
        return super().form_valid(form)

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article/article_detail.html'
    
class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'image','description','category', 'body','status',)
    template_name = 'article/article_edit.html'
    login_url = 'login' #new

    #Esto controla que un cualquier author NO edite los artículos que no le pertenece
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


"""
Esto elimina el artículo.
class ArticleDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login' #new
    

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
"""

#Esto es una eliminación lógica del artículo
@login_required(login_url='login')
def article_delete(request, slug):
    article =  get_object_or_404(Article, slug = slug)
    if request.method == 'POST':
        article =  get_object_or_404(Article, slug = slug)
        if article != None:
            article.delete = True
            article.save()
            return redirect('home')
        
    return render(request, 'article/article_delete.html',{'article':article})

