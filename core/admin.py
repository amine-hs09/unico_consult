from django.contrib import admin
from .models import Service, ClientMessage, Post

admin.site.register(Service)
admin.site.register(ClientMessage)
admin.site.register(Post)
