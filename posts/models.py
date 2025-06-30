"""
Defines the data models for the posts application.
"""

from django.db import models

class Post(models.Model):
    """
    Represents a post created by a user.
    """
    username = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the post.
        """
        return f"{self.title} - {self.username}"
