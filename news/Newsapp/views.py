from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def Index(request):
    newsapi=NewsApiClient(api_key='03da8debfe1e4d9f89d1202f0e360c65')
    topheadlines=newsapi.get_top_headlines(sources='google-news')

    articles=topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        mynewsapi=articles[i]

        news.append(mynewsapi['title'])
        desc.append(mynewsapi['description'])
        img.append(mynewsapi['urlToImage'])

    mylist=zip(news,desc,img)
    return render(request,'index.html',context={"mylist":mylist})



def bbc(request):
    newsapi=NewsApiClient(api_key='03da8debfe1e4d9f89d1202f0e360c65')
    topheadlines=newsapi.get_top_headlines(sources='bbc-news')

    articles=topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        mynewsapi=articles[i]

        news.append(mynewsapi['title'])
        desc.append(mynewsapi['description'])
        img.append(mynewsapi['urlToImage'])

    mylist=zip(news,desc,img)
    return render(request,'bbc.html',context={"mylist":mylist})

