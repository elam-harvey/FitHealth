from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_premium = models.BooleanField(default=False)

    # tell django to use the email to log in 
    USERNAME_FIELD = 'email'

    # tell django that the username field is not required
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email 

class UserProfile(models.Model):
    class GoalChoices(models.TextChoices):
        LOSE = 'lose weight', 'Lose Weight'
        GAIN = 'gain weight', 'Gain Weight'
        MAINTAIN = 'maintain weight', 'Maintain Weight'

    class ActivityChoices(models.TextChoices):
        SEDENTARY = 'sedentary', 'Sedentary'
        LIGHT = 'light', 'Light'
        MODERATE = 'moderate', 'Moderate'
        ACTIVE = 'active', 'Active'
        VERY_ACTIVE = 'very active', 'Very Active'

    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=20, choices=GoalChoices.choices)
    current_weight = models.FloatField(null=True, blank=True)
    target_weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=ActivityChoices.choices, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    medical_conditions = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.email} - {self.goal}"
    
    # to implement
    # subscriptions = models.ManyToManyField('Subscription', blank=True)
    """class LanguageChoices(models.TextChoices):
        ENGLISH = 'en', 'English'
        SPANISH = 'es', 'Spanish'
        FRENCH = 'fr', 'French'
        GERMAN = 'de', 'German'
        CHINESE = 'zh', 'Chinese'
        SWAHILI = 'sw', 'Kiswahili' """
    # preferred_language = models.CharField(max_length=20, default='en')

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #preferred_language = models.CharField(max_length=20, choices=LanguageChoices.choices, default='en')
    meal_reminders_time = models.TimeField(null=True, blank=True)
    notifications_enabled = models.BooleanField(default=True)
    dark_mode_enabled = models.BooleanField(default=False)
    hydration_reminders_enabled = models.BooleanField(default=False)