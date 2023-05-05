from django.db import models
from django.contrib.auth.models import User


class Incident(models.Model):
    INCIDENT_STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    incident_id = models.CharField(max_length=20, unique=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    reported_datetime = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    incident_status = models.CharField(max_length=15, choices=INCIDENT_STATUS_CHOICES)

    def __str__(self):
        return self.incident_id
