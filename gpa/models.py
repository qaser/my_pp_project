# TODO при добавлении времени наработки модели ГПА использовать
# значения по умолчанию привязанные к нагнетателю
import datetime as dt

from django.db import models
from django.db.models.deletion import CASCADE


class Engine(models.Model):
    title = models.CharField('марка двигателя', max_length=50)
    number_gg = models.CharField('заводской номер ГГ', max_length=20)
    number_st = models.CharField('заводской номер СТ', max_length=20)
    life_time = models.IntegerField(
        'наработка с начала эксплуатации',
        default=0
    )
    to_time = models.IntegerField('наработка после ТО')
    repair_time = models.IntegerField('наработка после ремонта')

    class Meta:
        verbose_name = 'двигатель'
        verbose_name_plural = 'двигатели'
        ordering = ('number_gg',)

    def __str__(self):
        return f'{self.title} - зав. номер: {self.number_gg}'


class Compressor(models.Model):
    title = models.CharField('марка нагнетателя', max_length=50)
    number = models.CharField('заводской номер', max_length=20)
    spch_type = models.CharField('тип СПЧ', max_length=10)
    life_time = models.IntegerField('наработка с начала эксплуатации')

    class Meta:
        verbose_name = 'нагнетатель'
        verbose_name_plural = 'нагнетатели'
        ordering = ('number',)

    def __str__(self):
        return f'{self.title} - зав. номер: {self.number}'


class Gpa(models.Model):
    STATUS_CHOICES = (
        ('work', 'Работа'),
        ('reserve', 'Резерв'),
        ('repair', 'Ремонт')
    )
    title = models.IntegerField('станционный номер ГПА')
    name = models.CharField('тип ГПА', max_length=50)
    engine = models.ForeignKey(
        Engine,
        on_delete=CASCADE,
        verbose_name='тип силовой установки',
        related_name='gpa',
        db_index=True,
    )
    compressor = models.ForeignKey(
        Compressor,
        on_delete=CASCADE,
        verbose_name='тип нагнетателя',
        related_name='gpa',
        db_index=True,
    )
    life_time = models.IntegerField('наработка с начала эксплуатации')
    kr_time = models.IntegerField('наработка после кап. ремонта')
    sr_time = models.IntegerField('наработка после среднего ремонта')
    status = models.TextField('состояние', choices=STATUS_CHOICES)


    class Meta:
        verbose_name = 'ГПА'
        verbose_name_plural = 'ГПА'
        ordering = ('title',)

    def __str__(self):
        return f'ГПА {self.title}'

    
class Flaw(models.Model):
    gpa = models.ForeignKey(
        Gpa,
        on_delete=CASCADE,
        verbose_name='ГПА',
        related_name='gpa',
        db_index=True,
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

    class Meta:
        verbose_name = 'неисправность'
        verbose_name_plural = 'неисправности'
        ordering = ('gpa',)

    def __str__(self):
        return f'{self.gpa} {self.text}'
