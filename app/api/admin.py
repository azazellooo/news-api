from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'vote']
    list_filter = ['author']
    search_fields = ['title']
    fields = ['id', 'title', 'author', 'created_at']
    readonly_fields = ['created_at', 'id',]

# Register your models here.
