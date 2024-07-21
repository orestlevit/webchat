from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_upload_to(obj, filename):
    return f"avatars/{filename}"

class SocialUser(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=avatar_upload_to, default="avatars/default.png")

    def __str__(self):
        return self.username
class TimeIt(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_ate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TimeIt):
    user_from = models.ForeignKey( SocialUser,on_delete=models.CASCADE)
    message = models.TextField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_from.username} -> {self.room.name}"


class Room(TimeIt):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(SocialUser)


    def get_other_user(self, current_user):
        return self.users.exclude(id=current_user.id).first()

    def __str__(self):
        return f"{self.name}"






