from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from articles.models import Article

from .pagination import ArticlesPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import (ArticlesSerializer, ArticleCreateSerializer, ArticleSerializer, ArticleUpdateSerializer)


class ArticlesAPIView(ListCreateAPIView):
    serializer_class = ArticleCreateSerializer
    pagination_class = ArticlesPagination
    queryset = Article.objects.is_publish()

    def get(self, request, *args, **kwargs):
        self.serializer_class = ArticleSerializer
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    queryset = Article.objects.all()

    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthorOrReadOnly]
        self.serializer_class = ArticleUpdateSerializer
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthorOrReadOnly]
        return self.destroy(request, *args, **kwargs)
