"""
Serializers for transforming Post model instances into JSON and vice versa.
"""

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Ensures 'username' is read-only after creation.
    """
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'created_datetime']

    def update(self, instance, validated_data):
        """
        Prevents updating the username after creation.
        """
        validated_data.pop('username', None)
        return super().update(instance, validated_data)