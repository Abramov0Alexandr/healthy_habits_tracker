from rest_framework import serializers
from habits.models import Habit
from habits.validators import DurationValidator, RelatedHabitAndRewardValidator, PleasureHabitValidator


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
        validators = [
            DurationValidator(field='duration'),
            RelatedHabitAndRewardValidator(),
            PleasureHabitValidator(field='is_pleasure'),
        ]
