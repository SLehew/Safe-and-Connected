from rest_framework import permissions


class IsManagerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        if request.user.role == "Client":
            return False
        return False
