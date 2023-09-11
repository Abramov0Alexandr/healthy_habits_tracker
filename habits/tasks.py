from datetime import datetime
import requests
from celery import shared_task
from notifiers import get_notifier
from config.settings import TG_ACCESS_TOKEN
from habits.models import Habit


def send_tg_notification(user_tg_username: str, message: str):
    telegram = get_notifier('telegram')
    request_url = f'https://api.telegram.org/bot{TG_ACCESS_TOKEN}/getUpdates'
    is_message_sent = False  # Флаг, указывающий, было ли отправлено сообщение

    response = requests.get(request_url)

    for i in response.json()['result']:

        if i['message'] and i['message']['from']:

            if i['message']['from'].get('username') == user_tg_username:

                user_tg_chat_id = i['message']['from'].get('id')
                telegram.notify(message=message, token=TG_ACCESS_TOKEN, chat_id=user_tg_chat_id)
                print(f'Пользователю {user_tg_username} отправлено напоминание')
                is_message_sent = True  # Устанавливаем флаг сообщения как отправленное
                break

    if not is_message_sent:  # Если флаг сообщения не был установлен, выводим информацию
        print(f'Пользователя с ником {user_tg_username} не обнаружено')


@shared_task()
def check_habit_execution_time():
    """
    Периодическая задача для отправки уведомлению пользователю.
    current_weekday: Информация о текущем дне недели.
    formatted_current_time: Текущее время в формате ЧЧ:ММ (12:00).

    Периодическая задача с интервалом в 1 минуту проверяет совпадение текущего времени (formatted_current_time) и
    времени выполнения привычки (habit_time).
    В случае, если worker обнаруживает совпадение, то вызывается функция 'send_tg_notification'.
    """

    current_weekday = datetime.now().weekday()
    full_current_time = datetime.now().time()
    formatted_current_time = f'{full_current_time.hour:02d}:{full_current_time.minute:02d}'

    all_habits = Habit.objects.all()

    for habit in all_habits:

        habit_time = f'{habit.time.hour:02d}:{habit.time.minute:02d}'

        user_tg_username = habit.user.tg_username
        notification_message = (f'Уже {habit_time}!\n'
                                f'Пора {habit.action} в {habit.place}')

        if habit.periodicity == 1:  # Каждые понедельник, среда, пятница

            if current_weekday in [0, 2, 4] and formatted_current_time == habit_time:
                send_tg_notification(user_tg_username=user_tg_username, message=notification_message)

        elif habit.periodicity == 2:  # Каждые вторник, четверг, суббота

            if current_weekday in [1, 3, 5] and formatted_current_time == habit_time:
                send_tg_notification(user_tg_username=user_tg_username, message=notification_message)

        elif habit.periodicity == 3:  # Каждый будний день

            if current_weekday in range(0, 5) and formatted_current_time == habit_time:
                send_tg_notification(user_tg_username=user_tg_username, message=notification_message)

        elif habit.periodicity == 4:  #: Каждые выходные

            if current_weekday in [5, 6] and formatted_current_time == habit_time:
                send_tg_notification(user_tg_username=user_tg_username, message=notification_message)

    print('В данный момент условий для оповещений нет')
