from django.contrib import admin
from .models import Events

# Register your models here.

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "club"]

    search_fields = ["name", "club"]
    ordering = ["date", "club"]
