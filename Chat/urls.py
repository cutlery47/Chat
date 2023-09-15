from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("Chat_Users.urls")),
    path('auth/', include('djoser.urls.authtoken')),
    path('chats/', include("Chat_Messages.urls")),
]
