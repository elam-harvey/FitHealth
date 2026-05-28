from django.contrib import admin
from .models import User, UserProfile, UserSettings


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserSettings)
