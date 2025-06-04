from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv

from .models import Message, Post, Service
from .forms import MessageForm, PostForm, ServiceForm

@login_required
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'portal/message_list.html', {'messages': messages})

@login_required
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    form = MessageForm(request.POST or None, instance=message)
    if form.is_valid():
        form.save()
        return redirect('message_list')
    return render(request, 'portal/message_form.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'portal/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'portal/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'portal/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'portal/post_confirm_delete.html', {'post': post})

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return redirect('service_update', pk=service.pk)
    return render(request, 'portal/service_form.html', {'form': form})

@login_required
def export_messages_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="messages.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'Subject', 'Status', 'Created'])
    for m in Message.objects.all():
        writer.writerow([m.user.username, m.subject, m.status, m.created_at])
    return response
