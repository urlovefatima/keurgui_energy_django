
from django.contrib import admin
from .models import Notification, Device

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'created_at', 'is_read')
    list_filter = ('type', 'is_read', 'created_at')
    search_fields = ('title', 'message')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'energy_consumption', 'active_since', 'percentage_change')
    list_filter = ('location',)
    search_fields = ('name', 'location')