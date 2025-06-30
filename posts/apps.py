"""
App configuration module for the posts application.
"""

from django.apps import AppConfig

class PostsConfig(AppConfig):
    """
    Configuration class for the posts app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
