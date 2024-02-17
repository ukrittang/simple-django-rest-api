from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class ArticleManager(models.Manager):
    def is_publish(self):
        qs = super(ArticleManager, self).filter(
            is_publish=True,
        )
        return qs


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=4000)
    created = models.DateTimeField(default=timezone.now, db_index=True)
    is_publish = models.BooleanField(default=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = ArticleManager()

    class Meta:
        ordering = ("-created",)
