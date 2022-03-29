
from django.db import models


# Create your models here.


class educator(models.Model):

    name = models.CharField('Преподаватель', max_length=128)

    # class Meta:
    #     ordering = ['name']
    #     verbose_name = 'Преподаватель'
    #     verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.name


class course(models.Model):

    educator = models.ForeignKey('userside.educator', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='courses')
    name = models.CharField('Название курса', max_length=128)
    length_of_time = models.IntegerField('Количество часов', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class mycourse(models.Model):

    name = models.ForeignKey('userside.course', on_delete=models.SET_NULL, null=True)
    date_begin = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')

    class Meta:
        ordering = ['name']
        verbose_name = 'Mой Курс'
        verbose_name_plural = 'Мои Курсы'

    def __str__(self):
        return self.name.name



