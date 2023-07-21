from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from mysite.settings.base import FORM_KEY
from .models import ContactMe
from .serializers import ContactMeSerializer
from .utils import email_sender


def index(request):
    return render(request, 'index.html')


class FrontendAPIAccessPermission(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('Planet')
        return api_key == FORM_KEY


class ContactMeViewSet(viewsets.ModelViewSet):
    permission_classes = [FrontendAPIAccessPermission]
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)  # call the original create method
        # send email after creating and validating an instance
        email_sender(request.data)
        return response
