from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetChats.as_view(), name='get_chats'),
    path('send/', views.SendMessage().as_view(), name='send_message'),
    path('<int:chat_id>', views.GetMessages.as_view(), name='get_messages'),
]