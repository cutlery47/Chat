from rest_framework import permissions
from Chat_Users.models import User

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request_data, view, obj):
        if 'user_id' in request_data:
            return request_data['user_id'] == str(obj.id)


class InChat(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # first we check if user_id is provided in the request
        if 'user_id' in request.data:
            # then we check if this user has the chat_id in "chats" attribute
            user = User.objects.get(pk=request.data['user_id'])
            # if so - permission granted
            for el in user.chats.all():
                if str(obj) == str(el.id):
                    return True

