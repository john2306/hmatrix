from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


# Create your models here.
STATUS_CHOICES = ( 
   ('individual', 'Individual'), 
   ('institution', 'Institution'), 
) 
class Project(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length=100, help_text='Una descripción breve del desafío')
    slug = models.SlugField(max_length=200, blank=True)
    overview = RichTextField('Describe el desafío.')
    bases = RichTextField('Describe las bases del desafío.')
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    publisher = models.CharField(max_length = 20, choices = STATUS_CHOICES, default ='institution') 
    status = models.BooleanField('Publicado/No publicado', default = True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)
