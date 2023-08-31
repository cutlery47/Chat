from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import Group

#check that the user exists (for the single user view)
def usercheck(user_id):
    try:
        return User.objects.get(pk=user_id)
    except:
        return None

# a view for retrieving multiple users data and adding a new user aswell
class UsersView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        #no permissions required
        all_users = User.objects.all()
        all_users_ser = UserSerializer(all_users, many=True)
        return Response(all_users_ser.data)

    def post(self, request):
        serilized_user = UserSerializer(data=request.data)
        if serilized_user.is_valid():
            data = serilized_user.validated_data
            new_user = User.objects.create_user(username=data['username'], first_name=data['first_name'],
                                     last_name=data['last_name'], password=data['password'],
                                     is_staff=data['is_staff'])
            #добавления созданного юзера в группу юзеров
            user_grp = Group.objects.get_by_natural_key(name="Regular")
            new_user.groups.add(user_grp)
            return Response(data)
        else:
            return Response(serilized_user.errors)


#a view for retrieving, editing and deleting single user data
class UserView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            #print(user.groups.values_list('id', flat=True).first())
            user_ser = UserSerializer(user)
            return Response(user_ser.data)
        else:
            return Response("USER NOT FOUND")

    def delete(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            user.delete()
            return Response("USER HAS BEEN SUCCESSFULLY DELETED")
        else:
            return Response("USER NOT FOUND")

    def put(self, request, **kwargs):
        user = usercheck(kwargs['user_id'])

        if user:
            user_ser = UserSerializer(instance=user, data=request.data)
            if user_ser.is_valid():
                user_ser.save()
                return Response("USER HAS BEEN UPDATED SUCCESSFULLY")
            else:
                return Response(user_ser.errors)
        else:
            return Response("USER NOT FOUND")

