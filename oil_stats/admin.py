from django.contrib import admin

from .models import Equip, Pump, Storage, Tank


class TankAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'volume', 'level')
    search_fields = ('title', 'location',)
    list_filter = ('title', 'location',)
    empty_value_display = '-пусто-'


class PumpAdmin(admin.ModelAdmin):
    list_display = ('operation', 'source', 'target', 'pump_date', 'quantity')
    search_fields = ('source', 'target', 'pump_date', 'quantity',)
    list_filter = ('operation',)
    empty_value_display = '-пусто-'


class EquipAdmin(admin.ModelAdmin):
    list_display = ('gpa', 'storage')
    search_fields = ('gpa', 'storage',)
    list_filter = ('gpa', 'storage',)
    empty_value_display = '-пусто-'


class StorageAdmin(admin.ModelAdmin):
    list_display = ('title', 'number')
    search_fields = ('title', 'number',)
    empty_value_display = '-пусто-'


admin.site.register(Tank, TankAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(Storage, StorageAdmin)