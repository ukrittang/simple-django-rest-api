from rest_framework.serializers import (
    ModelSerializer
)

from articles.models import Article


class ArticlesSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created',
        ]


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
            'created',
            'author',
        ]


class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]


class ArticleUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'is_publish',
        ]
