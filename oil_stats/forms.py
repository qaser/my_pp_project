from django import forms

from .models import Pump, Util, StrainerChange


class PumpForm(forms.ModelForm):
#    pump_date = forms.DateTimeField(input_formats=["%d.%m.%Y"])
    class Meta:
        model = Pump
        fields = ['operation', 'pump_date', 'source', 'target', 'quantity', 'maker']


# TODO добавить валидацию для значения util <= 0
class UtilForm(forms.ModelForm):
    class Meta:
        model = Util
        fields = ['source', 'day_date', 'util', 'reason', 'description']
#        widgets = {'description': forms.Textarea(attrs={'cols': 50})}


class StrainerChangeForm(forms.ModelForm):
    class Meta:
        model = StrainerChange
        fields = ['title', 'location', 'change_date', 'maker', 'description']
#        widgets = {'discription': forms.Textarea(attrs={'cols': 50})}
