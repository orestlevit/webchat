from django.contrib import admin

from core.models import Message, Room

sites = [Message, Room]

for i in sites:
    admin.site.register(i)



