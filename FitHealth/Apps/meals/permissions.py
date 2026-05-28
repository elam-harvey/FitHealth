from rest_framework import permissions


class IsPremiumOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only premium user to tweak the meal plans
    """

    def has_permission(self, request, view):
        # Allow read-only access for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to premium users
        return bool(request.user and request.user.is_authenticated and request.user.is_premium)