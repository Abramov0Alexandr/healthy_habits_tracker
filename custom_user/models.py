from django.contrib.auth.models import AbstractUser
from django.db import models
from custom_user.user_manager import CustomUserManager


NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    tg_username = models.CharField(max_length=50, unique=True, verbose_name='TG username')
    tg_chat_id = models.CharField(max_length=50, unique=True, verbose_name='TG chat-ID', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус активации')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
