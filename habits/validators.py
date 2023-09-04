from datetime import timedelta
from rest_framework import status
from rest_framework.serializers import ValidationError


class DurationValidator:
    """
    Класс для валидации поля 'duration' и 'reward'.
    При указании длительности выполнения привычки свыше 120 секунд возбуждается ошибка.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value.get(self.field, timedelta())
        total_duration_in_sec = duration.total_seconds()

        if total_duration_in_sec > 120:
            raise ValidationError(
                {
                    'message': "Время выполнения привычки не может превышать 120 секунд.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )


class RelatedHabitAndRewardValidator:
    """
    Класс для валидации полей 'related_habit' и 'reward'.
    Валидатор проверяет, недопустимость одновременного заполнения полей 'related_habit' и 'reward'.
    Валидатор проверяет, что связанная привычка 'related_habit' имеет положительный флаг 'is_pleasure'.
    """

    def __call__(self, value):
        related_habit = value.get('related_habit')
        reward = value.get('reward')

        if related_habit and reward:
            raise ValidationError(
                {
                    'message': "Не допускается одновременное указание приятной привычки и вознаграждения.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )

        if related_habit and not related_habit.is_pleasure:
            raise ValidationError(
                {
                    'message': "Связанная привычка должна быть приятной.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )


class PleasureHabitValidator:
    """
    Класс для валидации полей 'related_habit' и 'reward' у связанной (приятной) привычки.
    Валидатор проверяет, недопустимость заполнения поля 'reward' или указания связанной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        is_pleasure = value.get(self.field)
        related_habit = value.get('related_habit')
        reward = value.get('reward')

        if is_pleasure:
            if related_habit:
                raise ValidationError(
                    {
                        'message': "У приятной привычки не может быть связанной привычки.",
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )
            if reward:
                raise ValidationError(
                    {
                        'message': "У приятной привычки не может быть указано вознаграждение.",
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )
