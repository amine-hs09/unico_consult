from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Service, ClientMessage, Post


# Service views
class ServiceListView(ListView):
    model = Service


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['type', 'description']
    success_url = reverse_lazy('service_list')


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['type', 'description']
    success_url = reverse_lazy('service_list')


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service_list')


# ClientMessage views
class ClientMessageListView(ListView):
    model = ClientMessage


class ClientMessageDetailView(DetailView):
    model = ClientMessage


class ClientMessageCreateView(CreateView):
    model = ClientMessage
    fields = ['name', 'email', 'subject', 'message', 'status']
    success_url = reverse_lazy('clientmessage_list')


class ClientMessageUpdateView(UpdateView):
    model = ClientMessage
    fields = ['name', 'email', 'subject', 'message', 'status']
    success_url = reverse_lazy('clientmessage_list')


class ClientMessageDeleteView(DeleteView):
    model = ClientMessage
    success_url = reverse_lazy('clientmessage_list')


# Post views
class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'publication_date']
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'publication_date']
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
