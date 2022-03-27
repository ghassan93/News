from django.urls import path
from .views import CategoryNewsList,CategoryNewsDetail,NewsList,NewsDetail

urlpatterns=[
    path('category-news-list',CategoryNewsList.as_view(),name='category-news-list'),
    path('category-news-detail/<int:pk>',CategoryNewsDetail.as_view(),name='category-news-list'),
    
    path('news-list',NewsList.as_view(),name='news-list'),
    path('news-detail/<int:pk>',NewsDetail.as_view(),name='category-news-list'),
]