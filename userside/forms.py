
from django import forms

import userside.models
import datetime


class CourseEdit(forms.ModelForm):
    class Meta:
        model = userside.models.course
        fields = '__all__'


class CourseCreate(forms.ModelForm):

    class Meta:
        model = userside.models.course
        fields = '__all__'


class MyCourseCreate(forms.ModelForm):

    class Meta:
        model = userside.models.mycourse
        fields = '__all__'

    def clean(self):
        mod = self.cleaned_data['name']
        value_hous = mod.length_of_time
        date_0 = self.cleaned_data['date_begin']
        date_1 = self.cleaned_data['date_end']

        if date_0 < datetime.date.today():
            raise forms.ValidationError('неверная начальная дата обучения (задана в прошлом)')

        days =int(value_hous/2/7*5)
        # количество рабочих дней с учётом выходных, с ежедневной нагрузкой 2ч
        if date_1 < date_0 + datetime.timedelta(days=days):
            raise forms.ValidationError(f'Неверная конечная дата обучения, требуется минимум {days} '
                                        f'рабочих дня(ей) на курс')


class MyCourseEdit(forms.ModelForm):

    class Meta:
        model = userside.models.mycourse
        fields = '__all__'






