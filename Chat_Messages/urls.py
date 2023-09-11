from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetChatsView.as_view(), name='get_chats'),
    path('<int:chat_id>', views.GetAndSendMessagesView.as_view(), name='chat_interact'),
]