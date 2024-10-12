from django.db import models

# Create your models here.

class News(models.Model):
    news_headline = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    news_text = models.TextField()
    date_of_publication = models.DateField()
    slug = models.SlugField(null = False, unique=True)

    def __str__(self):
        return self.news_headline
