from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


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

    incident_id = models.CharField(primary_key=True, max_length=20, unique=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    reported_datetime = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    incident_status = models.CharField(max_length=15, choices=INCIDENT_STATUS_CHOICES)

    def __str__(self):
        return self.incident_id

    def save(self, *args, **kwargs):
        # Generate a random 5-digit number
        random_number = get_random_string(length=5, allowed_chars='1234567890')

        # Get the current year
        current_year = datetime.now().year

        # Construct the incident ID in the required format
        incident_id = f'RMG{random_number}{current_year}'

        # Set the incident ID if it's blank
        if not self.incident_id:
            self.incident_id = incident_id

        super().save(*args, **kwargs)
