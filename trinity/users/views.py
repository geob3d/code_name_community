from django.shortcuts import render
from users.models import UserInfo
from users.serializers import UserSerializer
from rest_framework import generics

# Create your views here.
class userListCreate(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer