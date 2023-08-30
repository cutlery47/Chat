from django.urls import path
from . import views

urlpatterns = [
    #для пользователя
    path("", views.getOrCreateUsers.as_view(), name='get_create_users'),
    path("<int:user_id>", views.retriveOrEditOrDeleteUser.as_view(), name='retrieve_single'),
]

