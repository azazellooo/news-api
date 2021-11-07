from rest_framework import serializers

from ..models import Post
from .comment import CommentSerializer
from .user import UserSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created_at', 'author', 'comments', 'vote')
        read_only_fields = ('id', 'author')


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'created_at',)
        read_only_fields = ('id',)
