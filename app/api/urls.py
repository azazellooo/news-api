from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentViewSet, PostUpvote, PostUnvote

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:pk>/upvote/', PostUpvote.as_view(), name='post-upvote'),
    path('post/<int:pk>/unvote/', PostUnvote.as_view(), name='post-unvote'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
