from django.contrib import admin
from Apps.community.models import Post, Comment, Like


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
