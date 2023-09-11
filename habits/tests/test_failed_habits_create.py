from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser


class HabitFailedCreateTestCase(APITestCase):
    """ТестКейсы для тестирования ситуаций, при которых возникают ошибки создания привычки"""

    def setUp(self) -> None:
        """Предварительное наполнение БД для дальнейших тестов."""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            tg_username='test_tg_username'
        )

        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_habit_with_pleasure_flag(self):
        """Тестирование создания привычки с положительным флагом 'is_pleasure' """

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
            "is_pleasure": True
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_required_fields_habit(self):
        """Тестирование создание привычки без указания обязательных полей ('related_habit' / 'reward') """

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_overflow_field_habit(self):
        """Тестирование создания привычки при одновременном указании награды и связанной привычки"""

        related_habit_data = {
            "place": "Тестовое место связанной привычки",
            "time": "12:00",
            "action": "Тестовое действие связанной привычки",
            "duration": "120",
        }

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
            "related_habit": related_habit_data,
            "reward": "Тестовая награда"
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_execution_time_habit(self):
        """Тестирование создания привычки с указанием времени исполнения, превышающим 120 секунд"""

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "130",
            "is_public": True,
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_execution_time_related_habit(self):
        """Тестирование создания привычки с указанием времени исполнения связанной привычки, превышающим 120 секунд"""

        related_habit_data = {
            "place": "Тестовое место связанной привычки",
            "time": "12:00",
            "action": "Тестовое действие связанной привычки",
            "duration": "130",
        }

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
            "related_habit": related_habit_data,
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
