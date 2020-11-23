import datetime as dt

from django.db import models
from django.db.models.deletion import CASCADE
from gpa.models import Gpa
from users.models import User


class Storage(models.Model):
    title = models.CharField('тип склада масел', max_length=50)
    number = models.CharField('станционный номер', max_length=10)

    def __str__(self):
        return f'{self.title} {self.number}'

# model for selecting equipment
# this is an intermediate model for grouping two models
# Gpa and Storage
class Equip(models.Model):
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
    pump_date = models.DateField('дата перекачки', default=dt.date.today)
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
    quantity = models.IntegerField('количество')
    maker = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='pump_maker',
        verbose_name='исполнитель'
    )
