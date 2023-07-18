from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Snippet
from .serializers import ContactMeSerializer


def index(request):
    return render(request, 'index.html')


class ContactMeViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = ContactMeSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
