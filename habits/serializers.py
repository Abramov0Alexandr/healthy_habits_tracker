from rest_framework import serializers
from habits.models import Habit


class HabitsCreateSerializers(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове POST запросов в контроллере HabitsCreateView
    user: автоматическое заполнение поля при создании экземпляра Привычки
    """

    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Habit
        fields = '__all__'
        # fields = ('user', 'place', 'time', 'action', 'is_pleasure', 'related_habit',
        #           'periodicity', 'reward',)


class HabitsListSerializers(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове GET запросов в контроллере HabitsListView
    """

    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = '__all__'
