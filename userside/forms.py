from django import forms

import userside.models


class CourseSearch(forms.Form):
    name = forms.CharField(label='Название курса', required=False)
    of_time = forms.IntegerField(label='Количество часов', required=False, help_text='Минимальное количество часов')
    educator = forms.ModelChoiceField(label='Препод', required=False, queryset=userside.models.educator.objects.all())

    # def clean(self):
    #     raise forms.ValidationError('Ошибка')

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
        # widgets = {
        #     'name': forms
        # }
