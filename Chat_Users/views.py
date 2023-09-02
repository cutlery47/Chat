from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from django import http

#check that the user exists (for the single user view)
def usercheck(user_id):
    try:
        return User.objects.get(pk=user_id)
    except:
        raise http.Http404

# a view for retrieving multiple users data and adding a new user aswell
class GetUsersView(APIView):
    #no permissions here
    def get(self, request):
        all_users = User.objects.all()
        all_users_ser = UserSerializer(all_users, many=True)
        return Response(all_users_ser.data)

class AddUserView(APIView):
    #allowed to register new acc id already registered
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serilized_user = UserSerializer(data=request.data)
        if serilized_user.is_valid():
            data = serilized_user.validated_data
            return Response(data)
        else:
            return Response(serilized_user.errors)

#a view for retrieving, editing and deleting single user data
class UserView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    # then, after recieving user from the usercheck(),
    # we have to explicitly call check_object_perm...
    # in order for it to check permissions
    def get(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            #print(user.groups.values_list('id', flat=True).first())
            self.check_object_permissions(request, user)
            user_ser = UserSerializer(user)
            return Response(user_ser.data)
        else:
            return Response("USER NOT FOUND")

    def delete(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            self.check_object_permissions(request, user)
            user.delete()
            return Response("USER HAS BEEN SUCCESSFULLY DELETED")
        else:
            return Response("USER NOT FOUND")

    def put(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            self.check_object_permissions(request, user)
            user_ser = UserSerializer(instance=user, data=request.data, partial=True)
            if user_ser.is_valid():
                user_ser.save()
                return Response("USER HAS BEEN UPDATED SUCCESSFULLY")
            else:
                return Response(user_ser.errors)
        else:
            return Response("USER NOT FOUND")

