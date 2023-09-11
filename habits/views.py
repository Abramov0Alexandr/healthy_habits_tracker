from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from habits.models import Habit
from habits.pagination import CustomPaginationClass
from habits.permissions import IsHabitCreator
from habits.serializers import HabitsCreateSerializers, HabitsListSerializers


class HabitsCreateView(generics.CreateAPIView):
    """
    Контроллер для создания нового экземпляра модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsCreateSerializers

    def perform_create(self, serializer):
        """
        Метод для автоматического определения текущего пользователя и заполнения поля 'creator'
        """

        new_habit = serializer.save(user=self.request.user)
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка экземпляров модели 'Привычка'
    Вызывается при GET запросах.
    """

    serializer_class = HabitsListSerializers
    pagination_class = CustomPaginationClass

    def get_queryset(self):

        if self.request.user.is_superuser:
            return Habit.objects.all()

        return Habit.objects.filter(user=self.request.user)


class PublicHabitsListView(generics.ListAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при GET запросах.
    """

    serializer_class = HabitsListSerializers
    pagination_class = CustomPaginationClass
    queryset = Habit.objects.filter(is_public=True)


class HabitsUpdateView(generics.UpdateAPIView):
    """
    Контроллер для отображения списка публичных экземпляров модели 'Привычка'.
    Вызывается при PUT/PATCH запросах.
    """

    serializer_class = HabitsCreateSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator | IsAdminUser]


class HabitsDeleteView(generics.DestroyAPIView):
    """
    Контроллер для удаления экземпляров модели 'Привычка'.
    Вызывается при DELETE запросах.
    """

    queryset = Habit.objects.all()
    permission_classes = [IsHabitCreator | IsAdminUser]
