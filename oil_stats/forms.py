from django import forms

from .models import Pump, Util, FilterChange


class PumpForm(forms.ModelForm):
    class Meta:
        model = Pump
        fields = ['operation', 'pump_date', 'source', 'target', 'quantity', 'maker']
        labels = {
            'operation': ('вид операции'),
            'pump_date': ('дата операции'),
            'source': ('откуда'),
            'target': ('куда'),
            'quantity': ('количество'),
            'maker': ('исполнитель'),
        }
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

# TODO добавить валидацию для значения util <= 0
class UtilForm(forms.ModelForm):
    class Meta:
        model = Util
        fields = ['source', 'day_date', 'util', 'reason', 'description']
#        widgets = {'description': forms.Textarea(attrs={'cols': 50})}


class FilterChangeForm(forms.ModelForm):
    class Meta:
        model = FilterChange
        fields = ['title', 'location', 'change_date', 'maker', 'description']
#        widgets = {'discription': forms.Textarea(attrs={'cols': 50})}
