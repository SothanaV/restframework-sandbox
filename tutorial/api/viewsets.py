from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import UserSerializer, GroupSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from .permissions import 

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    # queryset = User.objects.filter(username=request.user.username).order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        user = self.request.user
        print(user, type(user))
        if user.is_authenticated:
            return User.objects.filter(username=user.username)

class UserCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny, )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
