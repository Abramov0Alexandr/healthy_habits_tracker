from rest_framework import serializers
from habits.models import Habit
from habits.validators import DurationValidator, RelatedHabitAndRewardValidator, PleasureHabitValidator


class HabitsSerializers(serializers.ModelSerializer):
    """
    Сериализатор модели CustomUser.
    Используется при вызове POST запросов в контроллере HabitsCreateView
    user: автоматическое заполнение поля при создании экземпляра Привычки
    periodicity: отображение текстового описания выбранной периодичности
    """

    user = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)
    periodicity = serializers.ChoiceField(choices=Habit.PERIODICITY_CHOICES, source='get_periodicity_display')

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            DurationValidator(field='duration'),
            RelatedHabitAndRewardValidator(),
            PleasureHabitValidator(field='is_pleasure'),
        ]
