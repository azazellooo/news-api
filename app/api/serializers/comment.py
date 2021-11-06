from rest_framework import serializers
from ..models import Comment
from.user import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'created_at')
        read_only_fields = ('id', 'author')
