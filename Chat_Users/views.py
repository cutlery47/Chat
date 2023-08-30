from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

#представление для получения данных о всех юзерах и добавления пользователя
class getOrCreateUsers(APIView):
    def get(self, request):
        all_users = User.objects.all()
        all_users_ser = UserSerializer(all_users, many=True)
        return Response(all_users_ser.data)

    def post(self, request):
        serilized_user = UserSerializer(data=request.data)
        if serilized_user.is_valid():
            data = serilized_user.validated_data
            User.objects.create_user(username=data['username'], first_name=data['first_name'],
                                     last_name=data['last_name'], password=data['password'],
                                     is_staff=data['is_staff'])
            return Response(data)
        else:
            return Response(serilized_user.errors)

#представление для получения одного юзера, редактирования юзера, удаления юзера
class retriveOrEditOrDeleteUser(APIView):
    def usercheck(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None


    def get(self, request, **kwargs):
        user = self.usercheck(kwargs['user_id'])

        if user:
            user_ser = UserSerializer(user)
            return Response(user_ser.data)
        else:
            return Response("USER NOT FOUND")

    def delete(self, request, **kwargs):
        user = self.usercheck(kwargs['user_id'])

        if user:
            user.delete()
            return Response("USER HAS BEEN SUCCESSFULLY DELETED")
        else:
            return Response("USER NOT FOUND")

    def put(self, request, **kwargs):
        user = self.usercheck(kwargs['user_id'])

        if user:
            user_ser = UserSerializer(instance=user, data=request.data)
            if user_ser.is_valid():
                user_ser.save()
                return Response("USER HAS BEEN UPDATED SUCCESSFULLY")
            else:
                return Response(user_ser.errors)
        else:
            return Response("USER NOT FOUND")