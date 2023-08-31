from django.urls import path
from . import views

urlpatterns = [
    #users url
    path("", views.UsersView.as_view(), name='get_create_users'),
    path("<int:user_id>", views.UserView.as_view(), name='retrieve_single'),
]

