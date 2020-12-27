import datetime as dt
import django_tables2 as tables
from .models import Pump, StrainerChange, Util


class PumpTable(tables.Table):
    pump_date = tables.DateTimeColumn(format ='d.m.Y')

    class Meta:
        model = Pump
        exclude = ('id', )
        attrs = {'class': 'mytable'}


class StrainerChangeTable(tables.Table):
    change_date = tables.DateTimeColumn(format ='d.m.Y')

    class Meta:
        model = StrainerChange
        exclude = ('id', 'description',)
        attrs = {'class': 'mytable'}


class UtilTable(tables.Table):
    day_date = tables.DateTimeColumn(format ='d.m.Y')

    class Meta:
        model = Util
        exclude = ('id', 'description',)
        attrs = {'class': 'mytable'}
