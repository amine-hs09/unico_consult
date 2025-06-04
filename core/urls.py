from django.urls import path
from . import views

urlpatterns = [
    # Service URLs
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('services/<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # ClientMessage URLs
    path('messages/', views.ClientMessageListView.as_view(), name='clientmessage_list'),
    path('messages/create/', views.ClientMessageCreateView.as_view(), name='clientmessage_create'),
    path('messages/<int:pk>/', views.ClientMessageDetailView.as_view(), name='clientmessage_detail'),
    path('messages/<int:pk>/edit/', views.ClientMessageUpdateView.as_view(), name='clientmessage_update'),
    path('messages/<int:pk>/delete/', views.ClientMessageDeleteView.as_view(), name='clientmessage_delete'),

    # Post URLs
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
