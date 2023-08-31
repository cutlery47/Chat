from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

#создаю кастомную админку для работы с юзерами
class Admin(UserAdmin):
    #т.к. админка кастомная - в нее добавляем наши новые поля (только друзья пока что)
    add_fieldsets = (
        (None, {
            'Classes': ('wide',),
            'Fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')}
         ),
    )

    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'password', 'is_staff')}),
        ('Info', {'fields': ('email', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Friends', {'fields': ('friends', )})
    )

# Register your models here.
admin.site.register(User, Admin)