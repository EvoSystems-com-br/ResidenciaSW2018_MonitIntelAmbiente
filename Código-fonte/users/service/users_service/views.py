from .models import User, Camera
from rest_framework import generics

from .serializers import UserSerializer, CameraSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CameraList(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
