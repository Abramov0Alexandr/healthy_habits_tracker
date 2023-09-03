from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time', 'action', 'is_public',)
    list_display_links = ('user', )
