from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from fun.serializers import UserSerializer, GroupSerializer, JokeSerializer
from fun.models import Joke
from random import randint

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

def index(request):
	qs = Joke.objects.all()
	joke = qs.get(randint(0, len(qs)-1))
	args = { 'joke': joke.content }
	return render(request,'fun/index.html',args)
