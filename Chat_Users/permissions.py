from rest_framework import permissions

#if the user is admin - allowed editing data
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff

#editing allowed only if the user requests own data
class IsAuthenticatedAndOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if token was not provided or token is invalid
        if not request.user.is_authenticated:
            return False

        # if request method is GET, OPTIONS and smth else -- return the result
        if request.method in permissions.SAFE_METHODS:
            return True

        # if provided user id matches user id from the request -- return the result
        # basically it checks that user is trying to modify their own data
        return obj.id == request.user.id or request.user.is_staff
