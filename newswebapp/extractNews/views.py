from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
from .models import Article
import requests
import json


# Create your views here.
def index(request):
    article=Articles()
    print("-------FETCH WITH Author--------")
    article.fetchWithAuthor("David Murphy")
    print("Article count: ",article.getArticleCount())
    print("-------FETCH WITH Source--------")
    article.fetchWithSource('bbc-news,the-verge')
    print("Article count: ",article.getArticleCount())
    print("-------FETCH WITH DATES--------")
    article.fetchWithDates('2020-10-01','2020-10-12')
    print("Article count: ",article.getArticleCount())
    api=API()
    print("------LIST OF SOURCES-------")
    print(api.getListOfSources())
    print("------LIST OF AUTHORS--------")
    print(api.getListOfAuthors())
    return HttpResponse("Hello")

class Articles(object):
    total=0
    newsapi=""
    def __init__(self):
        Article.objects.all().delete()
        self.newsapi = NewsApiClient(api_key='28b3c6db134d4309ae66b07ce9e448c6')
    def getArticleCount(self):
        return self.total
    def getArticleCountBySource(self,source):
        fetchWithSource(source)
        return self.total
    def fetchWithDates(self,dateFrom,dateTo):
        Article.objects.all().delete()
        all_articles = self.newsapi.get_everything(q='apple',from_param=dateFrom,to=dateTo)
        self.total=all_articles["totalResults"]
        for articleDict in all_articles["articles"]:
            myArticle=Article()
            myArticle.sourceId=articleDict["source"]["id"]
            myArticle.sourceName=articleDict["source"]["name"]
            myArticle.author=articleDict["author"]
            myArticle.title=articleDict["title"]
            myArticle.description=articleDict["description"]
            myArticle.url=articleDict["url"]
            myArticle.urlToImage=articleDict["urlToImage"]
            myArticle.publishedAt=articleDict["publishedAt"]
            myArticle.content=articleDict["content"]
            myArticle.save()
    def fetchWithSource(self,source):
        Article.objects.all().delete()
        all_articles = self.newsapi.get_everything(sources=source)
        self.total=all_articles["totalResults"]
        for articleDict in all_articles["articles"]:
            myArticle=Article()
            myArticle.sourceId=articleDict["source"]["id"]
            myArticle.sourceName=articleDict["source"]["name"]
            myArticle.author=articleDict["author"]
            myArticle.title=articleDict["title"]
            myArticle.description=articleDict["description"]
            myArticle.url=articleDict["url"]
            myArticle.urlToImage=articleDict["urlToImage"]
            myArticle.publishedAt=articleDict["publishedAt"]
            myArticle.content=articleDict["content"]
            myArticle.save()
    def fetchWithAuthor(self,authorName):
        Article.objects.all().delete()
        self.total=0
        all_articles = self.newsapi.get_everything(q='apple')
        for articleDict in all_articles["articles"]:
            myArticle=Article()
            myArticle.sourceId=articleDict["source"]["id"]
            myArticle.sourceName=articleDict["source"]["name"]
            myArticle.author=articleDict["author"]
            myArticle.title=articleDict["title"]
            myArticle.description=articleDict["description"]
            myArticle.url=articleDict["url"]
            myArticle.urlToImage=articleDict["urlToImage"]
            myArticle.publishedAt=articleDict["publishedAt"]
            myArticle.content=articleDict["content"]
            if(myArticle.author==authorName):
                myArticle.save()
                self.total=self.total+1
class API(object):
    def getListOfSources(self):
        listOfSources=[]
        for item in Article.objects.values_list("sourceId"):
            if(item not in listOfSources):
                listOfSources.append(item)
        return listOfSources
    def getListOfAuthors(self):
        listOfAuthors=[]
        for item in Article.objects.values_list("author"):
            if(item not in listOfAuthors):
                listOfAuthors.append(item)
        return listOfAuthors