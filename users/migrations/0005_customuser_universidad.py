# Generated by Django 3.0.4 on 2020-03-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200308_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='universidad',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Universidad'),
        ),
    ]
