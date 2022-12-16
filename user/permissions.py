from rest_framework import permissions
from user.models import ApiToken

class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_TOKEN', '')
        return ApiToken.objects.filter(key=api_key).exists()
