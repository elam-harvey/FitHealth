from django.core.management.base import BaseCommand
from Apps.community.models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class Command(BaseCommand):
    help = 'creates sample posts and comments for testing and development purposes'

    def handle(self, *args, **kwargs):
        # get a user and attatch the post to them 
        try:
            existing_user = User.objects.get(email='hannyelam@gmail.com')
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User with the EMAIL Does not Exist'))
            return
        
        # create sample posts
        sample_posts = [
            {
                'title': 'My Fitness Journey',
                'content': 'I started my fitness journey a year ago and have lost 30 pounds!',
                'author': existing_user
            },
            {
                'title': 'Healthy Eating Tips',
                'content': 'Here are some tips for eating healthy on a budget.',
                'author': existing_user
            },
            {
                'title': 'Best Workouts for Weight Loss',
                'content': 'These workouts have helped me shed those extra pounds.',
                'author': existing_user
            }
        ]

        count = 0
        for post_data in sample_posts:
            post, created = Post.objects.get_or_create(**post_data)
            if created:
                count += 1
                self.stdout.write(self.style.SUCCESS(f'Created post: {post.title}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} posts.'))