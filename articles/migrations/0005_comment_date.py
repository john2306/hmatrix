# Generated by Django 3.0.4 on 2020-03-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200308_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
