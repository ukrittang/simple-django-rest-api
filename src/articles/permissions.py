from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    message = 'You must be the author of this article.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAccountOwner(BasePermission):
    message = "You must be the account owner."

    def has_object_permission(self, request, view, obj):
        return obj == request.user
