from django.urls import path, re_path
from .views import UserSettingsDetailView, UserProfileDetailView

urlpatterns = [
    # User Profile URLs
    path('me/', UserProfileDetailView.as_view(), name='user-profile'),
    path('update/', UserProfileDetailView.as_view(), name='user-profile-update'),
    # User Settings URLs
    path('settings/', UserSettingsDetailView.as_view(), name='user-settings'),
    path('settings/update/', UserSettingsDetailView.as_view(), name='user-settings-update'),
]