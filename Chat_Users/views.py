from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

#Не обращай внимания на подсветку objects - это пайчарм тупит
@api_view(['GET'])
def retrieveAllUsers(request):
    all_users = User.objects.all()
    serialized_all_users = UserSerializer(all_users, many=True)
    return Response(serialized_all_users.data)

@api_view(['GET'])
def retrieveSingleUser(request, user_id):
    user = User.objects.get(pk=user_id)
    serialized_user = UserSerializer(user, many=False)
    return Response(serialized_user.data)

@api_view(['POST'])
def addSingleUser(request):
    serilized_user = UserSerializer(data=request.data)
    if serilized_user.is_valid():
        serilized_user.save()
        return Response("New user has been successfully added!")
    else:
        return Response(serilized_user.errors)

@api_view(['POST'])
def updateSingleUser(request, user_id):
    user = User.objects.get(pk=user_id)
    serialized_user = UserSerializer(instance=user, data=request.data)
    if serialized_user.is_valid():
        serialized_user.save()
        return Response("The user has been updated successfully!")
    else:
        return Response(serialized_user.errors)

@api_view(['POST'])
def removeSingleUser(requst, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    return Response("The user has been removed successfully!")
