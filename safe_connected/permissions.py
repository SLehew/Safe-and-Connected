from rest_framework import permissions


# permission to allow only managers to create an event

class IsManagerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        if request.user.role == "Client":
            return False
        return False


# permission to allow only managers to edit event details

class IsManagerOrReadOnlyEventDetails(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


# permission to allow only managers to create an organization

class IsManagerOrReadOnlyCreateOrganiz(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


# permission to allow only managers to edit organization details

class IsManagerOrReadOnlyEditOrganiz(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.role == "Manager":
            return True
        return False


# permission to allow only managers to view clients list for their organiz

class IsManagerOnlyClientList(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "Manager":
            return True
        return False
