from django.urls import path
from .views import (ArticlesAPIView, ArticleAPIView)


urlpatterns = [
    path('', ArticlesAPIView.as_view()),
    path('<int:pk>/', ArticleAPIView.as_view()),
]
