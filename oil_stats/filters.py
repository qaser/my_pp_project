from django_filters.views import FilterView
import django_filters as df
from django_tables2.views import SingleTableMixin

from .models import Pump, Tank
from .tables import PumpTable
    

class PumpFilter(df.FilterSet):
    pump_date = df.DateFromToRangeFilter(label='Date (Between)')
    class Meta:
        model = Pump
        fields = ['operation', 'source', 'target',]
