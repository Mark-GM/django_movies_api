from rest_framework.permissions import BasePermission


class UserCanDeleteMovie(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Can-Delete").exists():
            return True
        return False
