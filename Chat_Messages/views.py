# Create your views here.
from rest_framework.views import APIView
from Chat_Messages import permissions
from . import services

#getting all the chats in which the current user is stated
#WARNING: get-request should always pass through a user_id!!!
class GetChatsView(APIView):
    """ Returns all the chats that the user is apart of """

    #no permissions here
    def get(self, request):
        services.getChats(request)


class GetAndSendMessagesView(APIView):
    """ Manages interaction between a user and a message chat """

    permission_classes = [permissions.InChat]

    def get(self, request, **kwargs):
        services.getMessages(request, self.check_object_permissions, kwargs['chat_id'])

    def post(self, request, **kwargs):
        services.sendMessages(request, self.check_object_permissions, kwargs['chat_id'])





