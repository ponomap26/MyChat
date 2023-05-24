from django.contrib import admin

# Register your models here.
from chatDRF.models import User, Message, Chat

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Chat)