import django_tables2 as tables
from .models import Pump, FilterChange, Util


class PumpTable(tables.Table):

    class Meta:
        model = Pump
        exclude = ('id', )
        attrs = {'class': 'mytable'}


class FilterChangeTable(tables.Table):

    class Meta:
        model = FilterChange
        exclude = ('id', 'description',)
        attrs = {'class': 'mytable'}


class UtilTable(tables.Table):

    class Meta:
        model = Util
        exclude = ('id', 'description',)
        attrs = {'class': 'mytable'}
