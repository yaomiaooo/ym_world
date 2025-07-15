from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         read_only_fields = ('created_at',)



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'