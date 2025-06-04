from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    STATUS_CHOICES = [
        ('NOUVEAU', 'Nouveau'),
        ('EN_COURS', 'En cours'),
        ('TRAITE', 'Traité'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='NOUVEAU')
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
