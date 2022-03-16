import datetime

from django.db import models

# Create your models here.


class educator(models.Model):
    name = models.CharField('ФИО', max_length=128)


class mycourse(models.Model):
    educator = models.ForeignKey('userside.educator', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='mycourses')
    name = models.CharField('Название курса', max_length=128)
    length_of_time = models.IntegerField('Количество часов', blank=True, null=True)
    status = models.CharField('Статус', max_length=128)
    mark = models.IntegerField('Оценка', blank=True, null=True)
    action_object = models.CharField('Действие над объектом', max_length=128)
    date_begin = models.DateField('Дата начала обучения')
    date_end = models.DateField('Дата окончания обучения')

    class Meta:
        ordering = ['length_of_time']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField()
    course = models.ManyToManyField('userside.mycourse')


# class Notice(models.Model):
#     new_notice = models.CharField('Уведомление')