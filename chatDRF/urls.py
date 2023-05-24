from django.urls import path
from chatDRF import views

urlpatterns = [
    path('api/user/', views.UserListCreateView.as_view()),
    path('api/chat', views.ChatListCreateView.as_view()),
    path('api/message', views.MassageListCreateView.as_view()),
]
