from django.urls import include, path
from . import views_account
from . import views_home
from . import views_profile
from . import views_events
from . import views_messaging
from . import views_news

urlpatterns = [
    # account related urls
    path('login_p1', views_account.login, name='login_p1'),
    path('register_p1', views_account.register, name='register_p1'),
    path('logout_p1', views_account.logout, name='logout_p1'),
    path('remove_p1', views_account.remove, name='remove_p1'),
    
    # home related urls
    path('home_p1', views_home.home, name='home_p1'),

    # profile related urls
    path('profile_p1', views_profile.profile, name='profile_p1'),
    path('create_profile_p1', views_profile.create_profile, name='create_profile_p1'),
    path('create_personal_p1', views_profile.create_personal, name='create_personal_p1'),
    path('create_educational_p1', views_profile.create_educational, name='create_educational_p1'),
    path('create_professional_p1', views_profile.create_professional, name='create_professional_p1'),
    path('view_profile_p1', views_profile.view_profile, name='view_profile_p1'),
    path('edit_profile_p1', views_profile.edit_profile, name='edit_profile_p1'),
    path('edit_personal_p1', views_profile.edit_personal, name='edit_personal_p1'),
    path('edit_educational_p1', views_profile.edit_educational, name='edit_educational_p1'),
    path('edit_professional_p1', views_profile.edit_professional, name='edit_professional_p1'),
    path('merge_p1', views_profile.merge, name='merge_p1'),

    # events related urls
    path('events_p1', views_events.events, name='events_p1'),
    path('event_generate_p1', views_events.event_generate, name='event_generate_p1'),
    path('event_list_p1', views_events.event_list, name='event_list_p1'),
    path('my_event_list_p1', views_events.my_event_list, name='my_event_list_p1'),
    
    # messaging related urls
    path('messaging_p1', views_messaging.messaging, name='messaging_p1'),

    # news related urls  
    path('news_technology_p1', views_news.news_technology, name='news_technology_p1'),
    path('news_science_p1', views_news.news_science, name='news_science_p1'),
    path('news_general_p1', views_news.news_general, name='news_general_p1'),
    path('news_entertainment_p1', views_news.news_entertainment, name='news_entertainment_p1'),
    path('news_sports_p1', views_news.news_sports, name='news_sports_p1'),
    path('news_business_p1', views_news.news_business, name='news_business_p1'),
]