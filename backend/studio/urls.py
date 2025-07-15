from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)  # 注册接口，地址会是 /api/articles/

urlpatterns = [
    path('api/save/', views.save_novel),
    path('', include(router.urls)),
    # path('articles/<int:pk>/toggle_favorite/', 
    #      views.ArticleViewSet.as_view({'post': 'toggle_favorite'}), 
    #      name='article-toggle-favorite'),
   

]



