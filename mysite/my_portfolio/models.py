from django.db import models


class Snippet(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    subject = models.TextField()
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

