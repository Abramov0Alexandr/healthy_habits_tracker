from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from custom_user.models import CustomUser
from habits.models import Habit


class HabitListTestCase(APITestCase):
    """ТестКейсы для тестирования отображения существующих привычек"""

    def setUp(self) -> None:
        """Предварительное наполнение БД для дальнейших тестов."""

        self.user = CustomUser.objects.create(
            email='user@email.dot',
            tg_username='test_tg_username'
        )

        self.private_habit = Habit.objects.create(
            user=self.user,
            place="Тестовое место",
            time="12:00",
            action="Тестовое действие",
            duration="120",
            reward="Тестовая награда"
        )

        self.public_habit = Habit.objects.create(
            user=self.user,
            place="Тестовое место для публичной привычки",
            time="12:00",
            action="Тестовое действие для публичной привычки",
            duration="120",
            reward="Тестовая награда для публичной привычки",
            is_public=True

        )

        """Имитация авторизации пользователя по JWT токену."""
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_habits_list(self):
        """Тестирование вывода списка существующих привычек"""

        response = self.client.get(reverse('habits:habits_list'))

        self.assertEqual(
            response.json(),
            {
                'count': 2,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.private_habit.id,
                            'user': 'user@email.dot',
                            'periodicity': 'Каждые понедельник, среда, пятница',
                            'related_habit': None,
                            'place': 'Тестовое место',
                            'time': '12:00:00',
                            'action': 'Тестовое действие',
                            'is_pleasure': False,
                            'reward': 'Тестовая награда',
                            'duration': '00:02:00',
                            'is_public': False
                        },
                        {
                            'id': self.public_habit.id,
                            'user': 'user@email.dot',
                            'periodicity': 'Каждые понедельник, среда, пятница',
                            'related_habit': None,
                            'place': 'Тестовое место для публичной привычки',
                            'time': '12:00:00',
                            'action': 'Тестовое действие для публичной привычки',
                            'is_pleasure': False,
                            'reward': 'Тестовая награда для публичной привычки',
                            'duration': '00:02:00',
                            'is_public': True
                        }
                    ]
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_public_habits_list(self):
        """Тестирование вывода списка существующих публичных привычек"""

        response = self.client.get(reverse('habits:public_habits_list'))

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.public_habit.id,
                            'user': 'user@email.dot',
                            'periodicity': 'Каждые понедельник, среда, пятница',
                            'related_habit': None,
                            'place': 'Тестовое место для публичной привычки',
                            'time': '12:00:00',
                            'action': 'Тестовое действие для публичной привычки',
                            'is_pleasure': False,
                            'reward': 'Тестовая награда для публичной привычки',
                            'duration': '00:02:00',
                            'is_public': True
                        }
                    ]
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
