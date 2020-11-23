from django.contrib import admin

from .models import Compressor, Engine, Flaw, Gpa


class EngineAdmin(admin.ModelAdmin):
    list_display = ('title', 'number_gg', 'number_st')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'


class CompressorAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'spch_type')
    search_fields = ('title',)
    list_filter = ('title', 'spch_type')
    empty_value_display = '-пусто-'


class GpaAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'engine', 'compressor')
    search_fields = ('title',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class FlawAdmin(admin.ModelAdmin):
    list_display = ('gpa', 'text', 'pub_date')
    search_fields = ('gpa', 'pub_date')
    list_filter = ('gpa', 'pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Engine, EngineAdmin)
admin.site.register(Compressor, CompressorAdmin)
admin.site.register(Gpa, GpaAdmin)
admin.site.register(Flaw, FlawAdmin)
