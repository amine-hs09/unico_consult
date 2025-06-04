from django.db import models


class Service(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type


class ClientMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
