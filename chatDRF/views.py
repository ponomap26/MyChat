from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from rest_framework import generics

from chatDRF.models import User, Chat, Message
from chatDRF.serializers import UserSerializer, ChatSerializer, MessageSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MassageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
