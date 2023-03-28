from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
]
