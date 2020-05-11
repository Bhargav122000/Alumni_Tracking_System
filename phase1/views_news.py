# this file includes functionality to display news related to several categories (phase1)

from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from datetime import date
from django.conf import settings
from newsapi import NewsApiClient
import datetime
import urllib.request
from os.path import realpath

# function to the url - 'news_technology_p1'
# functionality - to display a page containing Technology news (phase1)
def news_technology(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "technology" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"Technology"})
    else:
        return redirect('login_p1')

# function to the url - 'news_science_p1'
# functionality - to display a page containing Science news (phase1)
def news_science(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "science" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"Science"})
    else:
        return redirect('login_p1')

# function to the url - 'news_general_p1'
# functionality - to display a page containing General news (phase1)
def news_general(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "general" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"General"})
    else:
        return redirect('login_p1')

# function to the url - 'news_entertainment_p1'
# functionality - to display a page containing Entertainment news (phase1)
def news_entertainment(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "entertainment" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"Entertainment"})
    else:
        return redirect('login_p1')

# function to the url - 'news_sports_p1'
# functionality - to display a page containing Sports news (phase1)
def news_sports(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "sports" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"Sports"})
    else:
        return redirect('login_p1')

# function to the url - 'news_business_p1'
# functionality - to display a page containing Business news (phase1)
def news_business(request):
    if request.user.is_authenticated:
        newsapi = NewsApiClient(api_key ='4459863c473e4690b5043bd2a9008446') 

        getSources = newsapi.get_sources()

        name_list = []
        description_list = []
        url_list = []
        for item in getSources["sources"]:
            if(item["category"] == "business" and item["language"]=="en"):
                name_list.append(item["name"])
                description_list.append(item["description"])
                url_list.append(item["url"])
        mylist = zip(name_list, description_list, url_list)    
        return render(request,'phase1/news.html', {"mylist":mylist,"name":"Business"})
    else:
        return redirect('login_p1')
