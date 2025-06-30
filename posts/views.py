"""
API views for handling post-related operations (CRUD).
"""

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    Handles listing all posts and creating a new post.
    """
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

class PostUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a single post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Optionally override this method to customize the queryset.
        """
        return super().get_queryset()
