from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Novel

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()  # 获取所有文章
    serializer_class = ArticleSerializer  # 使用上面定义的转换器

#     def toggle_favorite(self, request, pk=None):
#         article = self.get_object()
#         article.is_favorite = not article.is_favorite
#         article.save()
#         return Response({'status': 'favorite toggled'})

@api_view(['POST'])
def save_novel(request):
    required_fields = ['title', 'content', 'character']
    if not all(field in request.data for field in required_fields):
        return Response({'message': '缺少必要字段'}, status=400)
    
    try:
        novel = Novel.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            character_id=request.data['character']
        )
        return Response({
            'id': novel.id,
            'title': novel.title,
            'created_at': novel.created_at
        })
    except Exception as e:
        return Response({'message': str(e)}, status=500)