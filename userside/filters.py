
import django_filters
import userside.models


class CourseFilter(django_filters.FilterSet):

    name = django_filters.Filter(lookup_expr='icontains', label='Название')
    educator = django_filters.Filter(lookup_expr='name__icontains',label='Преподаватель')

    class Meta:
        model = userside.models.course
        fields = '__all__'


class MyCourseFilter(django_filters.FilterSet):

    name = django_filters.Filter(lookup_expr='name__icontains', label='Название')

    class Meta:
        model = userside.models.mycourse
        fields = '__all__'

