# Generated by Django 3.0.4 on 2020-03-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200318_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
