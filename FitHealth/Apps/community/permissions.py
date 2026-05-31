from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Post, Comment


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the post or comment.
        if isinstance(obj, Post):
            return obj.author == request.user
        elif isinstance(obj, Comment):
            return obj.user == request.user

        return False