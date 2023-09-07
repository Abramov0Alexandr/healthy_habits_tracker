from rest_framework import generics
from habits.models import Habit
from habits.pagination import CustomPaginationClass
from habits.permissions import IsHabitCreator
from habits.serializers import HabitsSerializers


class HabitsCreateView(generics.CreateAPIView):
    """
    Контроллер для создания нового экземпляра модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsSerializers

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

    serializer_class = HabitsSerializers
    pagination_class = CustomPaginationClass

    def get_queryset(self):

        return Habit.objects.filter(user=self.request.user)


class PublicHabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsSerializers
    pagination_class = CustomPaginationClass
    queryset = Habit.objects.filter(is_public=True)


class HabitsUpdateView(generics.UpdateAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при PUT/PATCH запросах.
    """

    serializer_class = HabitsSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator]


class HabitsDeleteView(generics.DestroyAPIView):
    """
    Контроллер для удаления экземпляров модели 'Привычка'.
    Вызывается при DELETE запросах.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator]
