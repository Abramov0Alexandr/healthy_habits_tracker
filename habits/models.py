from django.contrib.auth import get_user_model
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    PERIODICITY_CHOICES = [
        (1, 'Каждые понедельник, среда, пятница'),
        (2, 'Каждые вторник, четверг, суббота'),
        (3, 'Каждый будний день'),
        (4, 'Каждые выходные')
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='creator', verbose_name='Пользователь')  # Создатель привычки

    place = models.CharField(max_length=255, verbose_name='Место выполнения')  # Место, где выполняется привычка

    time = models.TimeField(verbose_name='Время, когда выполняется привычка')  # Время, когда выполняется привычка

    action = models.CharField(max_length=255, verbose_name='Действие')  # Действие, представляющее привычку

    is_pleasure = models.BooleanField(default=False, verbose_name='Признак приятной привычки')

    related_habit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, **NULLABLE,
        related_name='main_habit', limit_choices_to={'is_pleasure': True},
        verbose_name="связанная привычка")  # Связанная привычка

    periodicity = models.PositiveIntegerField(default=1, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')

    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='Вознаграждение')  # Вознаграждение

    duration = models.DurationField(verbose_name='Длительность выполнения')  # Время на выполнение в минутах

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')  # Признак публичности

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)
