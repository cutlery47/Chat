from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

#получить всех пользователей
@api_view(['GET'])
def retrieveAllUsers(request):
    all_users = User.objects.all()
    serialized_all_users = UserSerializer(all_users, many=True)
    return Response(serialized_all_users.data)

#получить данные об одном пользователе
@api_view(['GET'])
def retrieveSingleUser(request, user_id):
    user = User.objects.get(pk=user_id)
    serialized_user = UserSerializer(user, many=False)
    return Response(serialized_user.data)

#добавить пользователя
@api_view(['POST'])
def addSingleUser(request):
    serilized_user = UserSerializer(data=request.data)
    if serilized_user.is_valid():
        data = serilized_user.data
        User.objects.create_user(username=data['username'], first_name=data['first_name'], last_name=data['last_name'],
                                 password=data['password'], is_staff=data['is_staff'])
        return Response("The user has been added successfully")
    else:
        return Response(serilized_user.errors)

#обновить данные пользователя
#мне очень стыдно но пока что я не знаю как сделать это по-другому...
#один огромный костыль
@api_view(['POST'])
def updateSingleUser(request, user_id):
    user = User.objects.get(pk=user_id)

    #пофиксить
    if 'password' not in request.data.keys():
        request.data['password'] = user.password

    serialized_user = UserSerializer(instance=user, data=request.data)

    if serialized_user.is_valid():
        user = serialized_user.save()
        user.set_password(user.password)
        user.save()
        return Response("The user has been updated successfully!")
    else:
        return Response(serialized_user.errors)

#удалить пользователя
@api_view(['POST'])
def removeSingleUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return Response("The user has been removed successfully!")

#получить друзей пользователя
@api_view(['GET'])
def retrieveUserFriends(request, user_id):
    user = User.objects.get(pk=user_id)
    friends = user.friends.all()
    serialized_friends = UserSerializer(friends, many=True)
    return Response(serialized_friends.data)