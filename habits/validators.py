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

    Валидатор проверяет, что хотя бы одно поле из необязательных ('related_habit' и 'reward')
    заполнено при создании нового экземпляра
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

        if not related_habit and not reward:
            raise ValidationError(
                {
                    'message': "Вы должны добавить связанную приятную привычку ('related_habit') "
                               "или указать награду ('reward')",
                    'status': status.HTTP_400_BAD_REQUEST
                },
            )


class RequiredFieldsValidator:
    """
    Класс для валидации полей у связанной привычки.

    Исключение возбуждается в следующих случаях:
    - у связанной привычки не указан флаг 'is_pleasure'
    - у связанной привычки указана награда
    - у связанной привычки указан положительный признак публичности
    - у связанной привычки уже имеется связанная привычка
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)

        if related_habit:

            if not related_habit.is_pleasure:
                raise ValidationError(
                    {
                        'message': "Связанная привычка должна быть приятной (is_pleasure=True)",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )

            if related_habit.reward:
                raise ValidationError(
                    {
                        'message': "У связанной приятной привычки не может быть награды",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )

            if related_habit.is_public:
                raise ValidationError(
                    {
                        'message': "Не допускается использовать публичные привычки",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )

            if related_habit.related_habit:
                raise ValidationError(
                    {
                        'message': "У связанной приятной привычки не может быть указана еще одна привычка",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )





