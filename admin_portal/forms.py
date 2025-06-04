from django import forms
from .models import Message, Post, Service

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body', 'status']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description']
