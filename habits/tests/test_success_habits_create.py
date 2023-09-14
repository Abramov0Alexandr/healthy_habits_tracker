from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser


class HabitCreateTestCase(APITestCase):
    """ТестКейсы для тестирования успешного создания привычки"""

    def setUp(self) -> None:
        """Предварительное наполнение БД для дальнейших тестов."""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            tg_username='test_tg_username'
        )

        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_habit_with_reward(self):
        """Тестирование создания привычки с указанием награды"""

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
            "reward": "Тестовая награда"
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                "id": 8,
                "user": "user@email.dot",
                "related_habit": None,
                "place": "Тестовое место",
                "time": "12:00:00",
                "action": "Тестовое действие",
                "is_pleasure": False,
                "periodicity": 1,
                "reward": "Тестовая награда",
                "duration": "00:02:00",
                "is_public": False
            }
        )

    def test_create_habit_with_related_habit(self):
        """Тестирование создания привычки с указанием связанной привычки"""

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
            "related_habit": related_habit_data
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
            format='json',  # Указываем формат данных
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                "id": 7,
                "user": "user@email.dot",
                "related_habit": {
                    "place": "Тестовое место связанной привычки",
                    "time": "12:00:00",
                    "action": "Тестовое действие связанной привычки",
                    "duration": "00:02:00"
                },
                "place": "Тестовое место",
                "time": "12:00:00",
                "action": "Тестовое действие",
                "is_pleasure": False,
                "periodicity": 1,
                "reward": None,
                "duration": "00:02:00",
                "is_public": False
            }
        )

    def test_create_public_habit(self):
        """Тестирование создания публичной привычки"""

        main_habit_data = {
            "place": "Тестовое место",
            "time": "12:00",
            "action": "Тестовое действие",
            "duration": "120",
            "is_public": True
        }

        response = self.client.post(
            reverse('habits:habits_create'),
            data=main_habit_data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 9,
                'user': 'user@email.dot',
                'related_habit': None,
                'place': 'Тестовое место',
                'time': '12:00:00',
                'action': 'Тестовое действие',
                'is_pleasure': False,
                'periodicity': 1,
                'reward': None,
                'duration': '00:02:00',
                'is_public': True
            }
        )
