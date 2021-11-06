from rest_framework import serializers

from ..models import Post
from .comment import CommentSerializer
from .user import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created_at', 'author', 'comments')
        read_only_fields = ('id', 'author')
