from django.contrib import admin

from .models import Equip, Util, Pump, Storage, Tank, FilterChange


class TankAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'volume', 'level')
    search_fields = ('title', 'location',)
    list_filter = ('title', 'location',)
    empty_value_display = '-пусто-'


class PumpAdmin(admin.ModelAdmin):
    list_display = (
        'operation',
        'source',
        'target',
        'pump_date',
        'quantity',
        'maker'
    )
    search_fields = ('source', 'target', 'pump_date', 'quantity',)
    list_filter = ('operation', 'source', 'target', 'pump_date',)
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


class UtilAdmin(admin.ModelAdmin):
    list_display = ('source', 'day_date', 'util', 'reason', 'description')
    search_fields = ('source', 'day_date', 'util', 'reason',)
    list_filter = ('source', 'day_date', 'util', 'reason',)
    empty_value_display = '-пусто-'


class FilterChangeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'change_date',
        'maker',
        'description'
    )
    search_fields = ('title', 'location', 'change_date', 'maker',)
    list_filter = ('title', 'location', 'change_date', 'maker',)
    empty_value_display = '-пусто-'


admin.site.register(Tank, TankAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Equip, EquipAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Util, UtilAdmin)
admin.site.register(FilterChange, FilterChangeAdmin)
