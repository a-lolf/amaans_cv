from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

router = DefaultRouter()
router.register(r'contact-me', views.ContactMeViewSet)

urlpatterns += router.urls
