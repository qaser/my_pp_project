from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import UtilForm, PumpForm, FilterChangeForm
from .models import Equip, Util, Pump, Storage, Tank, FilterChange, User
from .tables import PumpTable, UtilTable, FilterChangeTable


# function for split many posts on pages
def split_on_page(request, pump_page):
    paginator = Paginator(pump_page, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return {'page': page, 'paginator': paginator}


# функция для отображения начального экрана системы ГСМ
def index(request):
    pump_table = PumpTable(Pump.objects.all()[:5])
    filter_table = FilterChangeTable(FilterChange.objects.all()[:5])
    util_table = UtilTable(Util.objects.all()[:5])
    pump_form = PumpForm()
    util_form = UtilForm()
    filter_form = FilterChangeForm()
    return render(request, 'oil_stats/oil_index.html', {
            'pump_table': pump_table,
            'filter_table': filter_table,
            'util_table': util_table,
            'pump_form': pump_form,
            'util_form': util_form,
            'filter_form': filter_form
        }
    )


def pump_list(request):
    table = PumpTable(Pump.objects.all())
    return render(request, "oil_stats/pump_list.html", {
        'table': table
    })


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


def add_util(request):
    form = UtilForm(request.POST or None)
    if form.is_valid():
        source_id = form.cleaned_data['tank'].id
        util = form.cleaned_data['util']
        source_tank = get_object_or_404(Tank, id=source_id)
        # вычитаю из источника объем утечки масла
        source_tank.level = source_tank.level - util
        source_tank.save()
        form.save()
    return redirect('oil_index')


def add_filterchange(request):
    form = FilterChangeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('oil_index')
