from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class ValidationCheck(BasePermission):
    message = 'Access Denied Permission not granted.'

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        
        return obj.author==request.user
            