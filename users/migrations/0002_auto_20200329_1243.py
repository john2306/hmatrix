# Generated by Django 3.0.4 on 2020-03-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['date_creation']},
        ),
    ]
