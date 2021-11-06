from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers.post import PostSerializer
from .serializers.comment import CommentSerializer
from .permissions import PostDeleteUpdatePermission, CommentDeleteUpdatePermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostDeleteUpdatePermission]

    def get_permissions(self):
        if self.request.method in ('POST', 'GET'):
            return [AllowAny()]
        return super(PostViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentDeleteUpdatePermission]

    def get_permissions(self):
        if self.request.method in ('POST', 'GET'):
            return [AllowAny()]
        return super(CommentViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpvote(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.vote += 1
        post.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)


class PostUnvote(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.vote -= 1
        post.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)

# Create your views here.
