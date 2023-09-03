from rest_framework import generics
from habits.serializers import HabitsListSerializers, HabitsCreateSerializers
from habits.models import Habit


class HabitsCreateView(generics.CreateAPIView):
    """
    Контроллер для создания нового экземпляра модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsCreateSerializers


class HabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка экземпляров модели 'Привычка'
    Вызывается при GET запросах.
    """

    serializer_class = HabitsListSerializers
    queryset = Habit.objects.all()


class PublicHabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsCreateSerializers
    queryset = Habit.objects.filter(is_public=True)


class HabitsUpdateView(generics.UpdateAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при PUT/PATCH запросах.
    """

    serializer_class = HabitsListSerializers
    queryset = Habit.objects.all()


class HabitsDeleteView(generics.DestroyAPIView):
    """
    Контроллер для удаления экземпляров модели 'Привычка'.
    Вызывается при DELETE запросах.
    """

    queryset = Habit.objects.all()

