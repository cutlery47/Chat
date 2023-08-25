from django.urls import path
from . import views

urlpatterns = [
    path("", views.retrieveAllUsers, name='retrieve_all'),
    path("<int:user_id>", views.retrieveSingleUser, name='retrieve_single'),
    path("add/", views.addSingleUser, name='add_single'),
    path("remove/<int:user_id>", views.removeSingleUser, name='remove_single'),
    path("update/<int:user_id>", views.updateSingleUser, name='update_single'),
]

