from django.urls import path

from .views import AddPostApi, FollowBlogApi, NewsFeedListApi

urlpatterns = [
    path('blog/add_post/', AddPostApi.as_view(),
         name='add_post'),
    path('blog/<int:blog_id>/follow/', FollowBlogApi.as_view(),
         name='follow_blog'),
    path('blog/newsfeed/', NewsFeedListApi.as_view(),
         name='newsfeed_list')
]
