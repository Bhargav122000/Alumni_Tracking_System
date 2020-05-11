from django.urls import path
from . import views_account
from . import views_home
from . import views_alumni
from . import views_events
from . import views_messaging
from . import views_news

urlpatterns = [
    # account related urls
    path('login_p2', views_account.login, name='login_p2'),
    path('register_p2', views_account.register, name='register_p2'),
    path('logout_p2', views_account.logout, name='logout_p2'),
    path('remove_p2', views_account.remove, name='remove_p2'),

    # home related urls
    path('home_p2', views_home.home, name='home_p2'),

    # alumni related urls
    path('alumni_p2', views_alumni.alumni, name='alumni_p2'),
    path('requests_p2', views_alumni.requests, name='requests_p2'),
    path('gender_p2', views_alumni.gender, name='gender_p2'),
    path('branch_p2', views_alumni.branch, name='branch_p2'),
    path('year_p2', views_alumni.year, name='year_p2'),
    path('gender_year_p2', views_alumni.gender_year, name='gender_year_p2'),
    path('gender_branch_p2', views_alumni.gender_branch, name='gender_branch_p2'),
    path('branch_year_p2', views_alumni.branch_year, name='branch_year_p2'),
    path('branch_gender_year_p2', views_alumni.branch_gender_year, name='branch_gender_year'),
    path('all_list_p2', views_alumni.all_list, name='all_list_p2'),

    # events related urls
    path('events_p2', views_events.events, name='events_p2'),
    path('event_generate_p2', views_events.event_generate, name='event_generate_p2'),
    path('event_list_p2', views_events.event_list, name='event_list_p2'),
    path('my_event_list_p2', views_events.my_event_list, name='my_event_list_p2'),
    
    # messaging related urls
    path('messaging_p2', views_messaging.messaging, name='messaging_p2'),
    
    # news related urls
    path('news_technology_p2', views_news.news_technology, name='news_technology_p2'),
    path('news_science_p2', views_news.news_science, name='news_science_p2'),
    path('news_general_p2', views_news.news_general, name='news_general_p2'),
    path('news_entertainment_p2', views_news.news_entertainment, name='news_entertainment_p2'),
    path('news_sports_p2', views_news.news_sports, name='news_sports_p2'),
    path('news_business_p2', views_news.news_business, name='news_business_p2'),
    
]