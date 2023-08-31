from rest_framework import serializers
from .models import User

# можно наверное использовать дефолтные сериализаторы
# но пока что обойдусь Model сериализаторами
# потому что они просто удобнее и полегче

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 1) Сериализатор конвертирует жанговские модели и куерисеты в норальные форматы (например, жсон)
# 2) Десериализатор конвертирует нормальные форматы в жанговские модели
# 3) При вызове сериализатора мы подаем в объект сериализатора куерисет, при вызове десериализатора - жсоны
# 4) Сериализатор вызывается при get-запросах, десериализатор - при post-запросах
