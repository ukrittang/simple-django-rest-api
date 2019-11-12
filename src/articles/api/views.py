from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from articles.models import Article

from .pagination import ArticlesPagination
from .serializers import (ArticlesSerializer, ArticleSerializer, ArticleCreateSerializer, ArticleUpdateSerializer)


class ArticlesAPIView(ListAPIView):
    serializer_class = ArticlesSerializer
    permission_classes = [AllowAny]
    pagination_class = ArticlesPagination
    queryset = Article.objects.is_publish()


class ArticleAPIView(RetrieveAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    queryset = Article.objects.is_publish()


class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.is_publish()
    serializer_class = ArticleCreateSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )


class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.is_publish()
    serializer_class = ArticleUpdateSerializer


class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.is_publish()
