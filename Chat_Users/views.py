from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import IsAuthenticatedAndOwnerOrReadOnly
from . import services


class GetUsersView(APIView):
    """ Returns all the users' public data"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return services.getUsers()


class AddUserView(APIView):
    """ Adds a new user to a database """

    #allowed to register new acc id already registered
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return services.addUser(request)


class UserView(APIView):
    """ A view for retrieving, editing and deleting single user data """

    permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]
    # then, after recieving user from the usercheck(),
    # we have to explicitly call check_object_perm...
    # in order for it to check permissions

    def get(self, request, **kwargs):
        return services.getUser(request, self.check_object_permissions, kwargs['user_id'])

    def delete(self, request, **kwargs):
        return services.deleteUser(request, self.check_object_permissions, kwargs['user_id'])

    def put(self, request, **kwargs):
        return services.editUser(request, self.check_object_permissions, kwargs['user_id'])

class UserPostsView(APIView):
    """ A view for returning all the users' page posts """
    permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

    def get(self, request, **kwargs):
        return services.getPosts(request, self.check_object_permissions, kwargs['user_id'])

    def post(self, request, **kwargs):
        return services.addPosts(request, self.check_object_permissions, kwargs['user_id'])

    def delete(self, request, **kwargs):
        return services.deletePosts(request, self.check_object_permissions, kwargs['user_id'])