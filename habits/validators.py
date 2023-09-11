from datetime import timedelta
from rest_framework import status
from rest_framework.serializers import ValidationError


class DurationValidator:
    """
    Класс для валидации поля 'duration' у основной и связанной привычки.
    При указании длительности выполнения привычки свыше 120 секунд возбуждается ошибка.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        related_habit = value.get('related_habit')

        main_habit_duration = value.get(self.field, timedelta())
        main_habit_duration_in_sec = main_habit_duration.total_seconds()

        if main_habit_duration_in_sec > 120:
            raise ValidationError(
                {
                    'message': "Время выполнения привычки не может превышать 120 секунд.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )

        if related_habit:

            related_habit_duration = related_habit.get(self.field, timedelta())
            related_habit_duration_in_sec = related_habit_duration.total_seconds()

            if main_habit_duration_in_sec > 120 or related_habit_duration_in_sec > 120:
                raise ValidationError(
                    {
                        'message': "Время выполнения привычки не может превышать 120 секунд.",
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )


class InitialInstanceFieldsValidator:
    """
    Класс для валидации заполнения полей при создании экземпляра модели Привычка.

    Кейсы, при которых происходит вызов ошибки 'ValidationError':
        - в случае, если указывается положительный флаг 'is_pleasure' у основной привычки
        - в случае, если привычка не является публичной и у нее отсутствует информации о награде или связанной привычке
        - в случае, если одновременно указать награду и связанную привычку
    """

    def __call__(self, value):
        is_pleasure_habit = value.get('is_pleasure')
        related_habit = value.get('related_habit')
        reward = value.get('reward')

        if is_pleasure_habit:

            raise ValidationError(
                {
                    'message': "Недопустимо указывать признак приятной привычки у основной привычки",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )

        if not value.get('is_public'):
            if not (related_habit or reward):

                raise ValidationError(
                    {
                        'message': "Вы должны добавить связанную приятную привычку ('related_habit') "
                                   "или указать награду ('reward')",
                        'status': status.HTTP_400_BAD_REQUEST
                    },
                )

        if related_habit and reward:
            raise ValidationError(
                {
                    'message': "Не допускается одновременное указание награды и связанной привычки.",
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )
