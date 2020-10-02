from django.db import models

# Create your models here.
class Article(models.Model):
    sourceId=models.CharField(null=True, max_length=50)
    sourceName=models.CharField(max_length=50)
    author=models.CharField(null=True,max_length=50)
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=1000)
    url=models.CharField(max_length=200)
    urlToImage=models.CharField(null=True,max_length=200)
    publishedAt=models.CharField(max_length=50)
    content=models.CharField(null=True,max_length=500)