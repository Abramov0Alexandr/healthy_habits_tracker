from rest_framework.permissions import BasePermission


class IsHabitCreator(BasePermission):
    """
    Данный клас предоставляет право доступа создателю экземпляров класса 'Habit'.
    """

    def has_object_permission(self, request, view, obj):
        """
        Метод проверяет является ли текущий пользователь создателем привычки.

        :return: В результате проверки возвращаются булевые значения.
        В случае, если текущий пользователь создатель привычки (True) - то доступ разрешен.
        """

        if request.user == obj.user:
            return True

        return False
