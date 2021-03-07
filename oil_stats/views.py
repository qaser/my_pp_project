#from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django_tables2 import SingleTableMixin, LazyPaginator
from django_filters.views import FilterView
import pygal


from .filters import PumpFilter
from .forms import UtilForm, PumpForm, StrainerChangeForm
from .models import Equip, Util, Pump, Storage, Tank, StrainerChange
from .tables import PumpTable, UtilTable, StrainerChangeTable



# function for split many posts on pages
def split_on_page(request, pump_page):
    paginator = Paginator(pump_page, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return {'page': page, 'paginator': paginator}


# функция для отображения начального экрана системы ГСМ
@cache_page(60 * 15)
def index(request):
    pump_query = Pump.objects.all()[:5]
    strainer_query = StrainerChange.objects.all()[:5]
    util_query = Util.objects.all()[:5]
    pump_table = PumpTable(pump_query)
    strainer_table = StrainerChangeTable(strainer_query)
    util_table = UtilTable(util_query)
    return render(request, 'oil_stats/oil_index.html', {
            'pump_table': pump_table,
            'strainer_table': strainer_table,
            'util_table': util_table,
        }
    )


# @login_required
def add_pump(request):
    form = PumpForm(request.POST or None)
    if form.is_valid():
        # данные из формы можно извлечь так: form.cleaned_data['subject']
        source_id = form.cleaned_data['source'].id
        target_id = form.cleaned_data['target'].id
        quantity = form.cleaned_data['quantity']
        source_tank = get_object_or_404(Tank, id=source_id)
        target_tank = get_object_or_404(Tank, id=target_id)
        # вычитаю объем масла из источника
        source_tank.level = source_tank.level - quantity
        source_tank.save()
        # добавляю объем масла в целевой бак
        target_tank.level = target_tank.level + quantity
        target_tank.save()
        form.save()
        return redirect('oil_index')
    return render(request, 'oil_stats/add_pump.html', {'form': form})

def add_util(request):
    form = UtilForm(request.POST or None)
    if form.is_valid():
        source_id = form.cleaned_data['source'].id
        util = form.cleaned_data['util']
        source_tank = get_object_or_404(Tank, id=source_id)
        # вычитаю из источника объем утечки масла
        source_tank.level = source_tank.level - util
        source_tank.save()
        form.save()
        return redirect('oil_index')
    return render(request, 'oil_stats/add_util.html', {'form': form})


def add_strainer_change(request):
    form = StrainerChangeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('oil_index')
    return render(request, 'oil_stats/add_strainer_change.html', {'form': form})


class PumpListView(SingleTableMixin, FilterView):
    table_class = PumpTable
    paginator_class = LazyPaginator
    template_name = 'oil_stats/pump_list.html'
    filterset_class = PumpFilter


def pump_list(request):
    table = PumpTable(Pump.objects.all())
    data = [1, 4, 6, 8, 34, 68]
    graph = pygal.Bar().add('34567', )
    graph.add('some', data)
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    return render(request, 'oil_stats/pump_list.html', {
        'table': table,
        'graph': graph.render(),
    })
