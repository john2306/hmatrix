from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField('Teléfono:',max_length = 50,null=True, blank=True)
    universidad = models.CharField('Universidad:',max_length = 50,null = True, blank = True)
    photo = models.URLField('Foto de perfil (URL):',max_length=1000, default='https://pwcenter.org/sites/default/files/styles/profile_image/public/default_images/default_profile.png?itok=wW1obErD' ,
    help_text ='Pega el link de tu foto de: linkedin, facebook u otro. Le das click derecho a la imagen y seleccionas COPIAR DIRECCIÓN de la IMAGEN', 
    null=True, blank = True
    )
    slug = models.SlugField(max_length=255, blank=True, null = True)
    description = models.CharField('Descripción:',max_length =255, help_text='Una frase favorita o como de describe.', null = True, blank = True)
    bio = RichTextField('Biografía o Experiencia',null=True, blank=True)
    age = models.PositiveIntegerField('Edad:',null=True, blank=True)
    facebook = models.URLField('Facebook (url):', blank = True, null = True)
    linkedin = models.URLField('Linkedin (url):', blank = True, null = True)
    twitter = models.URLField('Twitter (url):', blank = True, null = True)
    instagram = models.URLField('Instagram (url):', blank = True, null = True)
    web = models.URLField('Web (url):', blank = True, null = True)
    estado = models.BooleanField('Autor Activo/No Activos', default=True)
    date_creation = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True, null= True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name +' '+self.last_name

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.slug)])