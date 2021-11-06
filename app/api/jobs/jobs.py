from ..models import Post
from datetime import datetime


def reset_votes():
    posts = Post.objects.all()
    posts.update(vote=0)
    print(f'votes reset {datetime.now()}')
