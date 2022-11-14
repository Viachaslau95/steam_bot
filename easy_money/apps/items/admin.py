from django.contrib import admin

from apps.items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'price_4', 'price_for_name_tag', 'is_active']
    list_editable = ['is_active']
