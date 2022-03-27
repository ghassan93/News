from rest_framework import generics
from news_app.models import CategoryNews,News
from .serializers import CategoryNewsSerializers,NewsSerializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import NewsUserOrReadOnly,AdminOrReadOnly


class CategoryNewsList(generics.ListAPIView):
    serializer_class = CategoryNewsSerializers
    queryset= CategoryNews.objects.all()
    permission_classes = [AdminOrReadOnly] 
    
class  CategoryNewsDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset=CategoryNews.objects.all()
    serializer_class=CategoryNewsSerializers
    permission_classes = [IsAdminUser]  
    
    
class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializers
    queryset= News.objects.all()
    permission_classes = [NewsUserOrReadOnly] 
    
class  NewsDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset=News.objects.all()
    serializer_class=NewsSerializers
    permission_classes = [IsAuthenticated]      