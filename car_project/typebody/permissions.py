from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Пользователь может создавать типы кузовов только при авторизации.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated