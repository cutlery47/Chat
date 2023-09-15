from .serializers import ChatSerializer
from .serializers import MessageSerializer
from Chat_Users.models import User
from .models import Message
from .models import Chat
from rest_framework.response import Response
from django import http

#check if chat exists
def chatcheck(chat_id):
    try:
        return Chat.objects.get(pk=chat_id)
    except:
        raise http.Http404

def getChats(request):
    # check if user_id is passed in the request
    if 'user_id' not in request.data:
        raise http.Http404

    # check if the user with specified user_id exists in the database
    try:
        owner = User.objects.get(pk=request.data['user_id'])
    except:
        return Response("REQUESTED USER NOT FOUND")

    # getting and returning every chat for selected user
    chats = []
    for chat in owner.chats.all():
        chats.append(ChatSerializer(chat).data)

    return Response(chats)

def getMessages(request, check_object_permissions, chat_id):
    # check if chat exists
    chatcheck(chat_id)

    # check if user is in the chat
    check_object_permissions(request, chat_id)

    # get all the message with the current chat_id from the database
    messages = Message.objects.filter(chat_id=chat_id)

    # we'll be returning a hashmap for easier data retrieval on the frontend
    # the only value of a hashmap is an array of messages
    return_messages = {'messages': None}
    chat_messages = []

    for msg in messages:
        chat_messages.append(MessageSerializer(msg).data)

    return_messages['messages'] = chat_messages
    return Response(return_messages)

def sendMessages(request, check_object_permissions, chat_id):
    # check if chat exists
    chatcheck(chat_id)

    # check if user is in the chat
    check_object_permissions(request, chat_id)

    # get the message from the request
    message = MessageSerializer(data=request.data)
    if message.is_valid():
        message.save()
    else:
        print(message.errors)

    return Response()