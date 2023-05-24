from django.urls import path
from chatApi import views
from chatApi.views import MessageDetail, MessageList, ChatDetail, ChatList, UserList

urlpatterns = [
    path('api/user/', views.UserList.as_view()),
    path('api/chat', views.ChatList.as_view()),
    path('api/message', views.MessageList.as_view()),
    path('api/profile', views.UserProfileList.as_view()),
    path('users/', UserList.as_view()),
    path('chats/', ChatList.as_view()),
    path('chats/<int:pk>/', ChatDetail.as_view()),
    path('messages/', MessageList.as_view()),
    path('messages/<int:pk>/', MessageDetail.as_view()),

]
