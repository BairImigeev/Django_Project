
import django_filters

import userside.models


class CourseFilter(django_filters.FilterSet):

    name = django_filters.Filter(lookup_expr='icontains', label='Название')
    print('фильтр : ', name)

    class Meta:
        model = userside.models.course
        fields = '__all__'
