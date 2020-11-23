import datetime as dt

from django.db import models
from django.db.models.deletion import CASCADE
from gpa.models import Gpa


class Storage(models.Model):  # склад масел или БПМ
    title = models.CharField('тип склада масел', max_length=50)
    number = models.CharField('станционный номер', max_length=10)

    def __str__(self):
        return f'{self.title} {self.number}'


class Equip(models.Model):  # модель для выбора ГПА или БПМ
    gpa = models.ForeignKey(
        Gpa,
        on_delete=CASCADE,
        verbose_name='ГПА',
        related_name='gpa_equip',
        blank=True,
        null=True
    )
    storage = models.ForeignKey(
        Storage,
        on_delete=CASCADE,
        verbose_name='БПМ или склад ГСМ',
        related_name='storage_equip',
        blank=True,
        null=True
    )

    def __str__(self):
        if self.gpa is None:
            return str(self.storage)
        return str(self.gpa)


class Tank(models.Model):
    title = models.CharField('тип маслобака', max_length=10)
    location = models.ForeignKey(Equip, on_delete=CASCADE, verbose_name='принадлежность')
    volume = models.IntegerField('емкость маслобака')
    level = models.IntegerField('уровень масла', null=True)

    def __str__(self):
        return f'{self.location} {self.title}'

class Pump(models.Model):
    OPERATION_CHOICES = (
        ('download', 'Скачка'),
        ('upload', 'Закачка'),
        ('pumping', 'Перекачка')
    )
    operation = models.CharField(
        'вид операции',
        max_length=10,
        choices=OPERATION_CHOICES
    )
    source = models.ForeignKey(
        Tank,
        on_delete=CASCADE,
        verbose_name='откуда',
        related_name='source'
    )
    target = models.ForeignKey(
       Tank,
        on_delete=CASCADE,
        verbose_name='куда',
        related_name='target'
    )
    pump_date = models.DateField('дата перекачки', default=dt.date.today)
    quantity = models.IntegerField('количество')