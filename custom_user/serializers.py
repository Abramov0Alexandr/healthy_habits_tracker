from rest_framework import serializers
from custom_user.models import CustomUser


class CustomUserListSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове GET запросов в контроллере CustomUserListView
    """

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове GET запросов в контроллере CustomUserCreateView
    """

    class Meta:
        model = CustomUser
        fields = ('password', 'email', 'tg_username',)

    def create(self, validated_data):
        """
        :param validated_data: Данные, переданные при создании нового пользователя
        Метод переопределен для корректного создания нового пользователя.
        Пароль указанный при создании пользователя хэшируется, появляется возможность авторизации по JWT.
        :return: Создается новый экземпляр класса CustomUser
        """

        new_custom_user = CustomUser.objects.create_user(**validated_data)
        return new_custom_user
