from django import forms

import userside.models


class CourseSearch(forms.Form):
    name = forms.CharField(label='Название курса', required=False)
    of_time = forms.IntegerField(label='Количество часов', required=False, help_text='Минимальное количество часов')

    def clean(self):
        cleaned_data = self.cleaned_data
        of_time = cleaned_data.get('of_time')

        if of_time and of_time > 100000:
            raise forms.ValidationError('Количество часов не должно быть больше 100000')

        return cleaned_data


class CourseEdit(forms.ModelForm):
    class Meta:
        model = userside.models.mycourse
        fields = '__all__'
