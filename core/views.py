from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View

from core.models import Room, Message


# Create your views here.

class ChatView(LoginRequiredMixin, TemplateView):
    template_name = "chat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = get_object_or_404(Room, id=self.kwargs["room_id"])
        if self.request.user not in room.users.all():
            return redirect("rooms")
        context["room"] = room
        context["messages"] = Message.objects.filter(room=room)
        return context


class ChatDataView(LoginRequiredMixin, View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        if request.user not in room.users.all():
            return JsonResponse({
                "error": "You are not a member of this room"
            }, status=403)
        messages = Message.objects.filter(room=room)
        other_user = room.get_other_user(request.user)
        return render(
            request,
            "chat.html", {
                "room": room,
                "message": messages,
                "other_user": other_user
            }
        )


class RoomListView(LoginRequiredMixin, ListView):
    template_name = "rooms.html"
    model = Room
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["rooms_with_users"] = [
            (room, room.get_other_user(user)) for room in self.get_queryset()]
        return context

    def get_queryset(self):
        user = self.request.user
        return Room.objects.filter(users__in=[user])
