from rest_framework import generics
from habits.models import Habit
from habits.serializers import HabitsCreateSerializers


class HabitsCreateView(generics.CreateAPIView):
    """
    Контроллер для создания нового экземпляра модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsCreateSerializers

    def perform_create(self, serializer):
        """
        Метод для автоматического определения текущего пользователя и заполнения поля 'lesson_owner'
        """

        new_habit = serializer.save(user=self.request.user)
        new_habit.lesson_owner = self.request.user
        new_habit.save()


class HabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка экземпляров модели 'Привычка'
    Вызывается при GET запросах.
    """

    serializer_class = HabitsCreateSerializers
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

    serializer_class = HabitsCreateSerializers
    queryset = Habit.objects.all()


class HabitsDeleteView(generics.DestroyAPIView):
    """
    Контроллер для удаления экземпляров модели 'Привычка'.
    Вызывается при DELETE запросах.
    """

    queryset = Habit.objects.all()

