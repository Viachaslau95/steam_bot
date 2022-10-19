from django.contrib import admin

from apps.items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price_3', 'price_4', 'is_active', 'is_testing']
    list_editable = ['is_active']