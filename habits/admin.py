from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'action', )
    list_display_links = ('action', )
