from django.db import models
from django.core.validators import EmailValidator


class ContactMe(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.EmailField(
        validators=[EmailValidator],
        help_text='Please enter a valid email address.',
    )
    subject = models.TextField()
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

