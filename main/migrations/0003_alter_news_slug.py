# Generated by Django 5.1.1 on 2024-09-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
