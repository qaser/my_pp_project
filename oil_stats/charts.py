import pygal
from .models import Pump

class PumpBar():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        self.chart.title= "Pump Graph"

    def get_data(self):
        data = {}
        for pump in Pump.objects.all():
            data[str(pump.target)] = int(pump.quantity)
        return data  # возвращается словарь {название: значение}

    def generate(self):
        chart_data = self.get_data()  # это словарь

        for key, value in chart_data.items():
            self.chart.add(key, value)  # pygal.Pie(**kwargs).add(key, value)

        return self.chart.render(is_unicode=True)
