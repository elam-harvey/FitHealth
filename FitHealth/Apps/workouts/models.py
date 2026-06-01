from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Workout(models.Model):
    image = models.ImageField(upload_to='workout_images/')
    video = models.FileField(upload_to='workout_videos/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.FloatField()  # Duration in minutes
    calories_burned = models.FloatField()
    category = models.CharField(max_length=100)
    importance = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.description}"

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans', null=True, blank=True)
    name = models.CharField(max_length=255)
    workouts = models.ManyToManyField(Workout, related_name='workout_plans')

    def __str__(self):
        return self.name
    
# Maps Workouts to Workout Plans
class WorkoutPlanItem(models.Model):
    DAY_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    TIME_OF_DAY = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='items')
    day_of_week = models.CharField(max_length=20, choices=DAY_OF_WEEK)
    time_of_day = models.CharField(max_length=20, choices=TIME_OF_DAY)
