"""
URL configuration for webchat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core import views
from core.views import UserListView, ListFriendView, SendRequestView, AcceptRequestsView, RejectRequestsView, \
    CancelRequestsView, RemoveFriendView, FriendRequestView
from webchat import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rooms/<int:room_id>', views.ChatView.as_view()),
    path("registration/", views.RegistrationView.as_view()),
    path("authorization/", LoginView.as_view(template_name="authorization.html")),
    path('logout/', LogoutView.as_view()),
    path('rooms/<int:room_id>', views.ChatDataView.as_view(), name="chat_data"),
    path('rooms/', views.RoomListView.as_view(), name="rooms"),
    path('send-friend-request/', SendRequestView.as_view(), name="send_friend_request"),
    path('users/', UserListView.as_view(), name="user_list"),
    path('friends/', ListFriendView.as_view(), name="friends"),
    path('accept-friend-request/<int:pk>/', AcceptRequestsView.as_view(), name="accept_friend_request"),
    path('reject-friend-request/<int:pk>/', RejectRequestsView.as_view(), name="reject_friend_request"),
    path('cancel-friend-request/<int:pk>', CancelRequestsView.as_view(), name="cancel_request"),
    path('remove-friend/<int:pk>', RemoveFriendView.as_view(), name="remove_friend"),
    path('friend-requests/', FriendRequestView.as_view(), name="friend_requests")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
