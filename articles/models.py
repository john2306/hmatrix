from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

CATEGORY_CHOICES = [
    ('general','General'),
    ('datascience','Ciencia de datos'),
    ('neurociencia','Neurociencia'),
    ('projects','Proyectos'),
]
# Create your models here.
class Article(models.Model):
    title = models.CharField('Título:',max_length = 255)
    description = models.CharField('Descripción:',max_length = 255, null=True, blank=True, help_text = 'Descripción corto del artículo o frases relevantes de la misma.')
    image = models.URLField('Imagen de portada (URL)', 
    default ='https://www.karlosperu.com/wp-content/uploads/2019/09/conectividad.png', 
    blank = True, null = True,
    help_text = 'Buscar imagen relacionado al artículo y pegar aquí la dirección URL de la imagen.'
    )
    slug = models.SlugField(max_length=300, blank=True, null = True)
    category = models.CharField('Categoría',max_length = 20, choices = CATEGORY_CHOICES, default = 'general', null =  True, blank = True)
    body = RichTextField('Contenido:',null=True, blank=True, help_text ='Publicar, en cualquier momento puede editarlo.')
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE) 
    delete = models.BooleanField('Borrado/No borrado', default = False)
    status = models.BooleanField('Publicar/No publicar', default = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.slug)])


class Comment(models.Model):
    article  = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'comments',)
    comment = models.CharField(max_length = 140)
    author = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL,null = True)
    date = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    status = models.BooleanField(default = True)
    
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
