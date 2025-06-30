"""
URL configuration for the posts API endpoints.
"""

from django.urls import path
from .views import PostListCreateAPIView, PostUpdateDeleteAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:id>/', PostUpdateDeleteAPIView.as_view(), name='post-update-delete'),
]
