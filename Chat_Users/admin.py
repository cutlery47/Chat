from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

#создаю кастомную админку для работы с юзерами
class Admin(UserAdmin):
    #т.к. админка кастомная - в нее добавляем наши новые поля (только друзья пока что)
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'friends')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')}
         ),
    )

# Register your models here.
admin.site.register(User, Admin)