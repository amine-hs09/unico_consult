from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_update, name='message_update'),
    path('messages/export/', views.export_messages_csv, name='export_messages_csv'),

    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('services/<int:pk>/edit/', views.service_update, name='service_update'),
]
