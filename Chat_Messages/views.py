# Create your views here.
from .serializers import ChatSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from Chat_Users.models import User
from .models import Message
from .models import Chat
from django import http
from Chat_Messages import permissions
from .serializers import MessageSerializer

#check if chat exists
def chatcheck(chat_id):
    try:
        return Chat.objects.get(pk=chat_id)
    except:
        raise http.Http404

#getting all the chats in which the current user is stated
#WARNING: get-request should always pass through a user_id!!!
class GetChats(APIView):
    permission_classes = [permissions.IsOwner]

    def get(self, request):
        data = request.data
        if 'user_id' not in data:
            raise http.Http404

        try:
            owner = User.objects.get(pk=data['user_id'])
            self.check_object_permissions(data, owner)
        except:
            return Response("REQUESTED USER NOT FOUND")

        #getting every chat for selected user
        chats = []
        for chat in owner.chats.all():
            chats.append(ChatSerializer(chat).data)

        return Response(chats)

class SendMessage(APIView):
    permission_classes = [permissions.InChat]

    def post(self, request):
        chatcheck(request.data['chat'])

        self.check_object_permissions(request, request.data['chat'])

        message = MessageSerializer(data=request.data)

        if message.is_valid():
            message.save()
        else:
            print(message.errors)

        return Response()

class GetMessages(APIView):
    permission_classes = [permissions.InChat]

    def get(self, request, **kwargs):
        req_chat_id = kwargs['chat_id']

        #check if chat exists
        chatcheck(req_chat_id)

        #check if user is in the chat
        self.check_object_permissions(request, req_chat_id)

        messages = Message.objects.filter(chat_id=req_chat_id)
        response = []

        for msg in messages:
            response.append(MessageSerializer(msg).data)

        return Response(response)
