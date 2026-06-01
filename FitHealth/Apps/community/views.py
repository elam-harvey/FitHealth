from rest_framework import viewsets, status
from .models import Like, Post, Comment
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @extend_schema(
        request=None, # Tells Swagger: "Do NOT show any textboxes or inputs!"
        responses={200: dict}
    )
    # use the @action decorator to create a custom endpoint for liking a post
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])

    # this endpoint will toggle the like status of the post for the authenticated user
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        like_queryset = Like.objects.filter(post=post, user=user)

        if like_queryset.exists():
            # if the like already exists, remove it (unlike)
            like_queryset.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            # if the like does not exist, create it (like)
            Like.objects.create(post=post, user=user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
