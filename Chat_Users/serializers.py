from rest_framework import serializers
from .models import User
from .models import UserPost
from django.contrib.auth.models import Group

# можно наверное использовать дефолтные сериализаторы
# но пока что обойдусь Model сериализаторами
# потому что они просто удобнее и полегче

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #called when making a PUT-request
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if 'password' in validated_data:
            instance.set_password(validated_data.get('password'))
        instance.save()

        return instance

    # called when making a POST-request
    def create(self, validated_data):
        # new user doesn't have any of these attributes
        # actually a hack -- needs to be fixed
        validated_data.pop('groups')
        validated_data.pop('user_permissions')
        validated_data.pop('friends')
        validated_data.pop('chats')

        # makes user active upon creating an instance
        validated_data['is_active'] = True
        new_user = User.objects.create_user(**validated_data)
        return new_user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = "__all__"


# 1) Сериализатор конвертирует жанговские модели и куерисеты в норальные форматы (например, жсон)
# 2) Десериализатор конвертирует нормальные форматы в жанговские модели
# 3) При вызове сериализатора мы подаем в объект сериализатора куерисет, при вызове десериализатора - жсоны
# 4) Сериализатор вызывается при get-запросах, десериализатор - при post-запросах
