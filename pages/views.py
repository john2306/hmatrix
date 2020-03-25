from django.views.generic import ListView, DetailView # new
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator  import Paginator
from articles.models import Article


# Create your views here.


def home(request):
    queryset = request.GET.get("buscar")
    articles = Article.objects.filter(status = True, delete = False)
    if queryset and articles:
        articles = Article.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains =  queryset),
            status = True,
            delete = False
            
        ).distinct()

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'home.html', {'articles':articles})


# Create your views here.
def datascience_view(request):
    queryset = request.GET.get("buscar")
    articles = Article.objects.filter(category = 'datascience', status = True)
    if queryset and articles:
        articles = Article.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains =  queryset),
            category = 'datascience',
            status = True
            
        ).distinct()

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'home.html', {'articles':articles})

# Create your views here.
def neurociencia_view(request):
    queryset = request.GET.get("buscar")
    articles = Article.objects.filter(category = 'neurociencia',status = True)
    if queryset and articles:
        articles = Article.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains =  queryset),
            category = 'neurociencia',
            status = True
            
        ).distinct()

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'home.html', {'articles':articles})

# Create your views here.
def education_view(request):
    queryset = request.GET.get("buscar")
    articles = Article.objects.filter(category = 'projects', status = True)
    if queryset and articles:
        articles = Article.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains =  queryset),
            category = 'projects',
            status = True
            
        ).distinct()

    paginator = Paginator(articles, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'home.html', {'articles':articles})

