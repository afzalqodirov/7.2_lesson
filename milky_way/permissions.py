from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, views, obj):
        return request.user and (request.user.is_staff or request.user == obj.user)
