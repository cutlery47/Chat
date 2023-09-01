from django.urls import path
from . import views

urlpatterns = [
    #users url
    path("", views.GetUsersView.as_view(), name='get__users'),
    path("add/", views.AddUserView.as_view(), name='add_user'),
    path("<int:user_id>", views.UserView.as_view(), name='retrieve_single'),
]

