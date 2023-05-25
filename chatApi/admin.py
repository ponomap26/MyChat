from django.contrib import admin

# Register your models here.
from chatApi.models import  Message, Chat, UserProfile

admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Chat)