from django import forms
from django.forms import widgets
from django_filters.views import FilterView
import django_filters as df
from django_tables2.views import SingleTableMixin
from django.contrib.admin.widgets import AdminDateWidget

from .models import Pump, Util, StrainerChange
from .tables import PumpTable
    

class PumpFilter(df.FilterSet):
    # pump_date = df.DateFromToRangeFilter(label='Date (Between)')
    pump_date = df.DateRangeFilter(label='Выберите период', choices=None)
    # date_range = df.DateFromToRangeFilter(label='Выберите промежуток времени')

    class Meta:
        model = Pump
        fields = ['operation', 'source', 'target', 'maker']  # 'date_range'


class UtilFilter(df.FilterSet):
    day_date = df.DateRangeFilter(label='Выберите период', choices=None)

    class Meta:
        model = Util
        fields = ['source', 'reason',]

class StrainerFilter(df.FilterSet):
    change_date = df.DateRangeFilter(label='Выберите период', choices=None)

    class Meta:
        model = StrainerChange
        fields = ['title', 'location', 'maker']
