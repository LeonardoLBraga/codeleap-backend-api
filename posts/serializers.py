"""
Serializers for transforming Post model instances into JSON and vice versa.
"""

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_datetime', 'username']
