from django.contrib import admin
from .models import User
from .models import UserPost
from django.contrib.auth.admin import UserAdmin

#создаю кастомную админку для работы с юзерами
class UsrAdmin(UserAdmin):
    #т.к. админка кастомная - в нее добавляем наши новые поля (только друзья пока что)
    add_fieldsets = (
        ('Info', {'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')}),
    )

    fieldsets = (
        ("ADASD", {'fields': ('username', 'first_name', 'last_name', 'password', 'is_staff')}),
        ('Info', {'fields': ('email', 'chats', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'user_permissions')}),
        ('Friends', {'fields': ('friends', )})
    )

# Register your models here.
admin.site.register(User, UsrAdmin)
admin.site.register(UserPost)
