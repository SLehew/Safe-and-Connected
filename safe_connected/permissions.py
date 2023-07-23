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


class IsManagerOrReadOnlyEventDetails(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


class IsManagerOrReadOnlyCreateOrganiz(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


class IsManagerOrReadOnlyEditOrganiz(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


class IsManagerOnlyClientList(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "Manager":
            return True
        return False
