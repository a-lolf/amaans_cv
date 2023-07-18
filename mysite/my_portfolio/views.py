from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ContactMe
from .serializers import ContactMeSerializer


def index(request):
    return render(request, 'index.html')


class ContactMeViewSet(viewsets.ModelViewSet):
    queryset = ContactMe.objects.all()
    serializer_class = ContactMeSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
