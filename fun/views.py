from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from fun.serializers import UserSerializer, GroupSerializer, JokeSerializer
from fun.models import Joke


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JokeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jokes to be viewed or edited.
    """
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
