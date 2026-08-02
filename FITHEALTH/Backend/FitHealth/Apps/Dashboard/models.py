from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Motivation(models.Model):
    quote = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.quote[:50]  # Return the first 50 characters of the quote
    
class Snack(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='snacks/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Exercises(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ActiveChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    progress_text = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    