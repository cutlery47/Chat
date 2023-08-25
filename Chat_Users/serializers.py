from rest_framework import serializers
from .models import User

# можно наверное использовать дефолтные сериализаторы
# но пока что обойдусь Model сериализаторами
# потому что они просто удобнее и полегче

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
