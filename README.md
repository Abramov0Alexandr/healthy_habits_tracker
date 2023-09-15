# Healthy Habits Tracker

Данное приложение предназначено для отслеживания ваших здоровых привычек и поможет вам поддерживать их.


## Стек технологий:
   - python
   - django
   - djangorestframework
   - djangorestframework-simplejwt
   - drf-yasg
   - django-cors-headers
   - celery
   - redis
   - eventlet
   - django-celery-beat
   - notifiers
   - coverage
   - flake8


## Установка
Прежде чем начать использовать Healthy Habits Tracker, убедитесь, что у вас установлен 
интерпретатор Python (версия не ниже 3.9):

Клонируйте репозиторий с помощью следующей команды:
   ```bash
   git clone git@github.com:Abramov0Alexandr/healthy_habits_tracker.git
   ```

Перейдите в директорию проекта:
   ```bash
   cd healthy_habits_tracker
   ```

Установите зависимости с помощью Poetry:

   ```bash
   poetry install
   ```

Создайте и примените миграции для базы данных:

На ОС Windows:
   ```bash
   python manage.py migrate
   ```

На ОС Linux/Unix:

   ```bash
   python3 manage.py migrate
   ```

Запустите сервер:
   ```bash
   python manage.py runserver
   ```

Теперь вы можете открыть Healthy Habits Tracker в вашем веб-браузере по адресу http://localhost:8000/.


## Создание Docker образа и запуск контейнера
Чтобы собрать Docker-образ, выполните следующую команду:
   ```bash
  docker build -t hh_tracker .
   ```

После того как образ будет собран, вы сможете запустить контейнер командой
   ```bash
  docker run hh_tracker
   ```

## Возможности API
Healthy Habits Tracker предоставляет следующие возможности:

- Создание, редактирование и удаление привычек.
- Отслеживание выполнения привычек по времени и месту.
- Установка наград за выполнение привычек.
- Отслеживание продолжительности выполнения привычек.
- Создание связанных привычек (например, "пить воду" и "сделать зарядку").
- Отправку напоминаний о привычке в Telegram (@healthy_habit_trecker_bot)
- API
- И многое другое!

## Получение уведомлений в Telegram
Приложение предоставляет возможность получать уведомление в Telegram.
Для этого, откройте профиль Telegram бота (@healthy_habit_trecker_bot) и нажмите кнопку '/start'.
Теперь, когда настанет время выполнять созданную вами привычку, вам придет уведомление в формате: <br>
'Уже 08:00! Пора делать зарядку в парке'

## Документация
Healthy Habits Tracker предоставляет API для взаимодействия с приложением. Документацию к API вы можете найти перейдя по:<br>
http://127.0.0.1:8000/swagger/ <br>
http://127.0.0.1:8000/redoc/

## Тестирование
Если вы хотите внести свой вклад в разработку Healthy Habits Tracker или запустить тесты, установите дополнительные зависимости для разработки, как указано в файле pyproject.toml.

Для запуска тестов используйте следующую команду:

   ```bash
   python manage.py test
   ```

## Лицензия
Healthy Habits Tracker распространяется по [MIT License](https://opensource.org/licenses/MIT).

## Контакты

Спасибо за использование Healthy Habits Tracker! Если у вас есть какие-либо вопросы или предложения, не стесняйтесь обращаться к нам.

Автор: [Alexandr Abramov <https://github.com/Abramov0Alexandr>]

Связь: [alexandr.abramovv@gmail.com]https://github.com/Abramov0Alexandr)

GitHub: [https://github.com/Abramov0Alexandr]
