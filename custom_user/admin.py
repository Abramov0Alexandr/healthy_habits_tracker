from django.contrib import admin
from custom_user.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'tg_username', 'tg_chat_id', )
    list_display_links = ('email', )
