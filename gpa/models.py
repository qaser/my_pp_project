import datetime as dt

from django.db import models
from django.db.models.deletion import CASCADE


class Engine(models.Model):
    title = models.CharField('марка двигателя', max_length=50)
    number_gg = models.CharField('заводской номер ГГ', max_length=20)
    number_st = models.CharField('заводской номер СТ', max_length=20)
    life_time = models.IntegerField('наработка с начала эксплуатации')
    to_time = models.IntegerField('наработка после ТО')
    repair_time = models.IntegerField('наработка после ремонта')

    def __str__(self):
        return f'{self.title} - зав. номер: {self.number_gg}'


class Compressor(models.Model):
    title = models.CharField('марка нагнетателя', max_length=50)
    number = models.CharField('заводской номер', max_length=20)
    spch_type = models.CharField('тип СПЧ', max_length=10)
    life_time = models.IntegerField('наработка с начала эксплуатации')

    def __str__(self):
        return f'{self.title} - зав. номер: {self.number}'


class Gpa(models.Model):
    title = models.IntegerField('станционный номер ГПА')
    name = models.CharField('тип ГПА', max_length=50)
    engine = models.ForeignKey(
        Engine,
        on_delete=CASCADE,
        verbose_name='тип силовой установки',
        related_name= 'engine',
    )
    compressor = models.ForeignKey(
        Compressor,
        on_delete=CASCADE,
        verbose_name='тип нагнетателя',
        related_name= 'compressor',
    )
    life_time = models.IntegerField('наработка с начала эксплуатации')
    kr_time = models.IntegerField('наработка после кап. ремонта')
    sr_time = models.IntegerField('наработка после среднего ремонта')

    def __str__(self):
        return f'ГПА {self.title}'


class Flaw(models.Model):
    gpa = models.ForeignKey(
        Gpa,
        on_delete=CASCADE,
        verbose_name='ГПА',
        related_name='gpa'
    )
    text = models.CharField(
        'замечание',
        help_text='введите текст замечания',
        max_length=500
    )
    pub_date = models.DateField(
        'дата обнаружения',
        default=dt.date.today,
    )
