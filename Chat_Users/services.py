from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from django import http

#check that the user exists (for the single user view)
def usercheck(user_id):
    try:
        return User.objects.get(pk=user_id)
    except:
        raise http.Http404

def getUsers():
    all_users = User.objects.all()
    all_users_ser = UserSerializer(all_users, many=True)
    return Response(all_users_ser.data)

def getUser(request, check_object_permissions, user_id):
    user = usercheck(user_id)

    if user:
        # print(user.groups.values_list('id', flat=True).first())
        check_object_permissions(request, user)
        user_ser = UserSerializer(user)
        return Response(user_ser.data)
    else:
        return Response("USER NOT FOUND")


def addUser(request):
    serilized_user = UserSerializer(data=request.data)
    if serilized_user.is_valid():
        data = serilized_user.validated_data
        return Response(data)
    else:
        return Response(serilized_user.errors)

def deleteUser(request, check_object_permissions, user_id):
    user = usercheck(user_id)

    if user:
        check_object_permissions(request, user)
        user.delete()
        return Response("USER HAS BEEN SUCCESSFULLY DELETED")
    else:
        return Response("USER NOT FOUND")

def editUser(request, check_object_permissions, user_id):
    user = usercheck(user_id)

    if user:
        check_object_permissions(request, user)
        user_ser = UserSerializer(instance=user, data=request.data, partial=True)
        if user_ser.is_valid():
            user_ser.save()
            return Response("USER HAS BEEN UPDATED SUCCESSFULLY")
        else:
            return Response(user_ser.errors)
    else:
        return Response("USER NOT FOUND")