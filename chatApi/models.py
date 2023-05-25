from django.contrib.auth.models import User
from django.db import models

# Создание моделей.
from django.db.models.fields import related





"""Модель пользователя."""


class UserProfile(models.Model):
    user = models.OneToOneField(User, max_length=30, related_name='profile', on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.user


"""Модель чата."""


class Chat(models.Model):
    name = models.CharField(max_length=30)
    members = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""Модель сообщения."""


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
