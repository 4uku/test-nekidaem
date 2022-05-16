from django.urls import path

from .views import UserNewsFeedListApi

urlpatterns = [
    path('blog/<str:username>/add_post/', UserNewsFeedListApi.as_view(),
         name='news_feed'),
]
