from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'action', 'related_habit')
    list_display_links = ('user', )
