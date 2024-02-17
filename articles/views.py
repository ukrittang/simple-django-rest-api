from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from articles.models import Article

from .pagination import ArticlesPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    ArticleCreateSerializer,
    ArticleSerializer,
    ArticlesSerializer,
    ArticleUpdateSerializer,
)


class ArticlesAPIView(ListCreateAPIView):
    serializer_class = ArticlesSerializer
    pagination_class = ArticlesPagination
    queryset = Article.objects.is_publish()

    def post(self, request, *args, **kwargs):
        self.serializer_class = ArticleCreateSerializer
        return self.create(request, *args, **kwargs)

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
