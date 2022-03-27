from rest_framework import serializers
from news_app.models import CategoryNews,News


 
class NewsSerializers (serializers.ModelSerializer):
    news_user=serializers.StringRelatedField(read_only=True)
    
    
    class Meta:
        model =News
        fields ='__all__'


class CategoryNewsSerializers(serializers.ModelSerializer):
    news=NewsSerializers(many=True,read_only=True)
    class Meta:
        model = CategoryNews
        fields ='__all__'
        
