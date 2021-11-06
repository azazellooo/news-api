from rest_framework import permissions


class DeleteUpdatePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in ('destroy', 'update'):
            return request.user.is_staff or obj.author == request.user

