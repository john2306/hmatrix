# Generated by Django 3.0.4 on 2020-03-18 03:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200311_1231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('general', 'General'), ('datascience', 'Ciencia de datos'), ('neurociencia', 'Neurociencia'), ('education', 'Educación')], default='general', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Publicar, en cualquier momento puede editarlo, si así lo cree conveniente.', null=True, verbose_name='Contenido:'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, help_text='Descripción corto del artículo o frases relevantes de la misma.', max_length=255, null=True, verbose_name='Descripción:'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.URLField(blank=True, default='https://www.karlosperu.com/wp-content/uploads/2019/09/conectividad.png', help_text='Buscar imagen relacionado al artículo y pegar aquí la dirección URL de la imagen.', null=True, verbose_name='Imagen de portada (URL)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Título:'),
        ),
    ]
