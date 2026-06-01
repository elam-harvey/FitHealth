from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AICoachViewset


router = DefaultRouter()
router.register(r'coach', AICoachViewset, basename='coach')

urlpatterns = [
    path('', include(router.urls)),
]