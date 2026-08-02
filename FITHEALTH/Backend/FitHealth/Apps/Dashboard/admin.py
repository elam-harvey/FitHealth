from django.contrib import admin
from .models import Motivation, Snack, Exercises, ActiveChallenge


admin.site.register(Motivation)
admin.site.register(Snack)
admin.site.register(Exercises)
admin.site.register(ActiveChallenge)