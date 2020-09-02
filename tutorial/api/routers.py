from django.urls import include, path
from rest_framework import routers
from .viewsets import UserViewSet, GroupViewSet, UserCreate

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'groups', GroupViewSet)
router.register(r'register',UserCreate, basename='createuser')