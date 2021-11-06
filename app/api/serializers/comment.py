from rest_framework import serializers
from ..models import Comment
from.user import UserSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'created_at', 'post')
        read_only_fields = ('id', 'author')
