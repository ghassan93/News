from django.db import models
from account.models import User


class CategoryNews(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

class News(models.Model):
    category =models.ForeignKey(CategoryNews,related_name='news',on_delete=models.CASCADE)
    news_user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body =models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
