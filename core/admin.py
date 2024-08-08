from django.contrib import admin

from core.models import Message, Room, SocialUser

sites = [Message, Room, SocialUser]

for i in sites:
    admin.site.register(i)



