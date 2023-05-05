from django.urls import path
from .views import IncidentList, IncidentDetail

urlpatterns = [
    path('incidents/', IncidentList.as_view(), name='incident-list'),
    path('incidents/<str:pk>/', IncidentDetail.as_view(), name='incident-detail'),
]
