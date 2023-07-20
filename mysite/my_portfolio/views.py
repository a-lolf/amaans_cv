from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from mysite.settings.base import FORM_KEY
from .models import ContactMe
from .serializers import ContactMeSerializer


def index(request):
    return render(request, 'index.html')


class FrontendAPIAccessPermission(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-Key')
        return api_key == FORM_KEY


class ContactMeViewSet(viewsets.ModelViewSet):
    permission_classes = [FrontendAPIAccessPermission]
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
