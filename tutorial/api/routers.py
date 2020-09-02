from django.urls import include, path
from rest_framework import routers
from .viewsets import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet)