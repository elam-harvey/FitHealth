from rest_framework import serializers
from .models import Like, Post, Comment

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    # this will be used to tell the frontend if the post is liked
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'created_at']

    def get_likes_count(self, obj)->int:
        return obj.likes.count()

    def get_comments_count(self, obj)->int:
        return obj.comments.count()
    
    def get_is_liked(self, obj)->bool:
        request = self.context.get('request')
        if request is None or not request.user.is_authenticated:
            return False
        
        # check if the authenticated user has liked the post
        return obj.likes.filter(id=request.user.id).exists()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['created_at']