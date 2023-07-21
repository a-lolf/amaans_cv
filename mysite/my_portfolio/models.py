from django.db import models
from django.core.validators import EmailValidator


class ContactMe(models.Model):
    firstname = models.CharField(max_length=32, blank=False, null=False)
    lastname = models.CharField(max_length=32)
    email = models.EmailField(
        validators=[EmailValidator],
        help_text='Please enter a valid email address.', blank=False, null=False
    )
    subject = models.TextField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    datetime = models.DateTimeField(auto_now_add=True)

