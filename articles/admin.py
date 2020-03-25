from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
from .models import Article, Comment


class CommentInline(admin.StackedInline): # new
    model = Comment

admin.site.register(Comment)

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article

class ArticleAdmin(ImportExportModelAdmin,admin.ModelAdmin): # new
    inlines = [
    CommentInline,
    ]
    search_fields = ['title']
    list_display = ('title', 'description','author','status','delete',)
    resources_class = ArticleResource


admin.site.register(Article, ArticleAdmin) # new


