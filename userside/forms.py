from django import forms

import userside.models
import datetime


class CourseSearch(forms.Form):
    name = forms.CharField(label='Название курса', required=False)
    of_time = forms.IntegerField(label='Количество часов', required=False, help_text='Минимальное количество часов')
    educator = forms.ModelChoiceField(label='Преподаватель', required=False, queryset=userside.models.educator.objects.all())

    def clean_of_time(self):
        cleaned_data = self.cleaned_data
        of_time = cleaned_data.get('of_time')

        if of_time and of_time > 25000:
            raise forms.ValidationError('Количество часов не должно быть больше 100000')

        return of_time


class CourseEdit(forms.ModelForm):
    class Meta:
        model = userside.models.course
        fields = '__all__'


class CourseCreate(forms.ModelForm):
    name = forms.CharField(label='Название', required=True)

    date_begin = forms.DateField(label="введите начальную дату обучения", required=True)
    date_end = forms.DateField(label="введите конечную дату обучения", required=True)

    def clean_date_begin_date_end(self):
        data_0 = cleaned_data['date_begin']
        data_1 = self.cleaned_data['date_end']
        if data_0 < datetime.date.today():
            raise forms.ValidationError('Invalid date - renewal in past')

        # Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data_1 > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Invalid date - renewal more than 4 weeks ahead')
        # Помните, что всегда надо возвращать "очищенные" данные.

        return data_0, data_1

    class Meta:
        model = userside.models.course
        fields = ['name', 'date_begin', 'date_end']
        # widgets = {
        #     'name': forms
        # }


# class CourseCreate(forms.Form):
#
#     name = forms.CharField(label='Название', required=False)
#     date_begin = forms.DateField(help_text="введите началльную дату обучения")
#     date_end = forms.DateField(help_text="введите конченую дату обучения")
#
#     def clean_date_begin(self):
#
#         data_0 = self.cleaned_data['date_begin']

        # Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом).
    #     if data_0 < datetime.date.today():
    #         raise forms.ValidationError('Invalid date - renewal in past')
    #
    #     return data_0
    #
    # def clean_date_end(self):
    #
    #     data_1 = self.cleaned_data['date_end']
    #     # Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
    #     if data_1 > datetime.date.today() + datetime.timedelta(weeks=4):
    #         raise forms.ValidationError('Invalid date - renewal more than 4 weeks ahead')
    #     # Помните, что всегда надо возвращать "очищенные" данные.
    #     return data_1