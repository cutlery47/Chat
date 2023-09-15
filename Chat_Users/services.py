from .serializers import UserSerializer
from .serializers import PostSerializer
from rest_framework.response import Response
from .models import User
from .models import UserPost
from django import http


def usercheck(user_id):
    # check that the user exists (for the single user view)
    try:
        return User.objects.get(pk=user_id)
    except:
        raise http.Http404

def getUsers():
    #getting all the users in the database
    all_users = User.objects.all()
    all_users_ser = UserSerializer(all_users, many=True)
    return Response(all_users_ser.data)

def addUser(request):
    #adding a user with provided data -- simple as that
    user_ser = UserSerializer(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return Response(user_ser.validated_data)
    else:
        return Response(user_ser.errors)

def getUser(request, check_object_permissions, user_id):
    #checking if user with the id from url exists
    user = usercheck(user_id)

    if user:
        # in this case request=request and obj=user
        check_object_permissions(request, user)
        user_ser = UserSerializer(user)
        return Response(user_ser.data)
    else:
        return Response("USER NOT FOUND")

def deleteUser(request, check_object_permissions, user_id):
    # checking if user with the provided id exists
    user = usercheck(user_id)

    if user:
        # checking for permissions
        # if user owns the account - he's able to delete it
        check_object_permissions(request, user)
        user.delete()
        return Response("USER HAS BEEN SUCCESSFULLY DELETED")
    else:
        return Response("USER NOT FOUND")

def editUser(request, check_object_permissions, user_id):
    # checking if user with the provided id exists
    user = usercheck(user_id)

    if user:
        check_object_permissions(request, user)
        # getting an instance of a database object so that we're not adding a new user but editing an existing one
        user_ser = UserSerializer(instance=user, data=request.data, partial=True)
        if user_ser.is_valid():
            user_ser.save()
            return Response(user_ser.validated_data)
        else:
            return Response(user_ser.errors)
    else:
        return Response("USER NOT FOUND")

def getPosts(request, check_object_permissions, user_id):
    # checking if user with provided id exists
    user = usercheck(user_id)

    if user:
        check_object_permissions(request, user)
        #we'll be returning a hashmap for easier data retrieval on the frontend
        #the only value of a hashmap is an array of posts
        return_posts = {'posts': None}
        user_posts = []

        # filling up the array
        for post in UserPost.objects.filter(user_id=user_id):
            user_posts.append(PostSerializer(post).data)

        return_posts['posts'] = user_posts
        return Response(return_posts)
    else:
        return Response("USER NOT FOUND")

def addPosts(request, check_object_permissions, user_id):
    #checking if user exists
    user = usercheck(user_id)

    if user:
        #checking if user is allowed to post on this page
        check_object_permissions(request, user)
        serialized_post = PostSerializer(data=request.data)
        if serialized_post.is_valid():
            #adding user id from token to the request
            serialized_post.validated_data['user_id'] = request.user.id
            serialized_post.save()
            return Response(serialized_post.validated_data['content'])
        else:
            return Response(serialized_post.errors)

    else:
        return Response("USER NOT FOUND")

def deletePosts(request, check_object_permissions, user_id):
    # checking if user exists
    user = usercheck(user_id)

    if not request.data.get('post_id'):
        return Response("POST ID NOT PROVIDED")

    if user:
        # checking if user is allowed to delete the post in the request
        check_object_permissions(request, user)
        post = UserPost.objects.get(pk=request.data['post_id'])

        # if user somehow manages to access post_id, which is not one of his post_ids
        # he'll get busted
        if post.user_id == request.user.id:
            post.delete()
        else:
            return Response("YOU ARE NOT ALLOWED TO DELETE THE POST")

        return Response("THE POST HAS BEEN SUCCESSFULLY DELETED")
    else:
        return Response("USER NOT FOUND")
