from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    link = models.CharField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    vote = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return f'{self.author}. {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null=False,
        blank=False
    )
    content = models.TextField(max_length=1500, null=False, blank=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

