from django.urls import path
from .views import (ArticlesAPIView, ArticleAPIView, ArticleCreateAPIView, ArticleUpdateAPIView, ArticleDeleteAPIView)


urlpatterns = [
    path('', ArticlesAPIView.as_view()),
    path('<int:pk>/', ArticleAPIView.as_view()),
    path('create/', ArticleCreateAPIView.as_view()),
    path('<int:pk>/update/', ArticleUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ArticleDeleteAPIView.as_view()),
]
