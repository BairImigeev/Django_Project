
import django_filters

import userside.models


class CourseFilter(django_filters.FilterSet):

    name = django_filters.Filter(lookup_expr='icontains', label='Название')
    print('фильтр : ', name)
    # date_begin  = django_filters.DateRangeFilter.

    class Meta:
        model = userside.models.course
        fields = '__all__'


# class DateFilter(django_filters.FilterSet):
#     date_begin = django_filters.Filter()


# class CourseDateFilter(django_filters.DateRangeFilter):
#     pass