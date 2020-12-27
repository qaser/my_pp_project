import datetime as dt
from django.conf import settings

from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE
from gpa.models import Gpa


class Storage(models.Model):
    title = models.CharField('тип склада масел', max_length=50)
    number = models.CharField('станционный номер', max_length=10)

    def __str__(self):
        return f'{self.title} {self.number}'


# model for selecting equipment.
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
    location = models.ForeignKey(
        Equip,
        on_delete=CASCADE,
        verbose_name='принадлежность',
        related_name='location'
    )
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
    operation = models.TextField(
        'вид операции',
        choices=OPERATION_CHOICES
    )
    pump_date = models.DateTimeField(
        'дата перекачки',
        default=dt.datetime.today
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
    quantity = models.IntegerField(
        'количество',
        validators=[MinValueValidator(1)]
    )
    maker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='pump_maker',
        verbose_name='исполнитель',
        null=True
    )

    class Meta:
        ordering = ('-pump_date',)

    def __str__(self):
        return (
            f'{self.operation} {self.quantity} литров масла '
            f'из {self.source} в {self.target}'
        )


class Util(models.Model):
    REASON_CHOICES = (
        ('day_util', 'суточный расход'),
        ('failure', 'авария'),
        ('repair', 'ремонт'),
        ('else', 'другое')
    )
    source = models.ForeignKey(
        Tank,
        on_delete=CASCADE,
        verbose_name='маслобак',
        related_name='tank'
    )
    day_date = models.DateTimeField(
        'дата регистрации',
        default=dt.datetime.today
    )
    util = models.IntegerField(
        'расход масла',
        null=True,
        validators=[MinValueValidator(1)]
    )
    reason = models.TextField(
        'причина расхода',
        choices=REASON_CHOICES
    )
    description = models.TextField(
        'примечание',
        max_length=500,
        null=True,
        blank=True,
        help_text='заполнить при необходимости'
    )

    class Meta:
        ordering = ('-day_date',)

    def __str__(self):
        return (
            f'{self.tank} | {self.day_date.strftime("%d.%m.%Y")} '
            f'расход масла составил: {self.util} л.'
        )


class StrainerChange(models.Model):
    title = models.CharField('фильтр', max_length=20)
    location = models.ForeignKey(
        Equip,
        on_delete=CASCADE,
        verbose_name='оборудование',
        related_name='filter'
    )
    change_date = models.DateTimeField(
        'дата замены',
        default=dt.datetime.today
    )
    maker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='change_maker',
        verbose_name='исполнитель',
        null=True
    )
    description = models.TextField(
        'примечание',
        max_length=500,
        null=True,
        blank=True,
        help_text='Например: тип фильтроэлемента, характер загрязнения'
    )

    class Meta:
        ordering = ('-change_date',)

    def __str__(self):
        return (
            f'{self.title}, {self.location} | '
            f'{self.change_date.strftime("%d.%m.%Y")} '
        )
