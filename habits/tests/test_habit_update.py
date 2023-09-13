from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from habits.models import Habit


class HabitUpdateTestCase(APITestCase):
    """ТестКейсы для тестирования изменения существующих привычек при вызове PUT/PATCH методов"""

    def setUp(self) -> None:
        """Предварительное наполнение БД для дальнейших тестов."""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            tg_username='test_tg_username'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place="Тестовое место",
            time="12:00",
            action="Тестовое действие",
            duration="120",
            is_public=True
        )

        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_patch_habit(self):
        """Тестирование обновления полей экземпляра класса 'Habit' при вызове PATCH запроса"""

        changed_data = {
            "place": "Новое измененное место",
            "action": "Новое измененное действие",
            "reward": "Новая тестовая награда"
        }

        response = self.client.patch(f'/habits/update/{self.habit.id}/', data=changed_data)
        self.maxDiff = None

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.id,
                "user": "user@email.dot",
                "related_habit": None,
                "place": "Новое измененное место",
                "time": "12:00:00",
                "action": "Новое измененное действие",
                "is_pleasure": False,
                "periodicity": 1,
                "duration": "00:02:00",
                "is_public": True,
                "reward": "Новая тестовая награда"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
