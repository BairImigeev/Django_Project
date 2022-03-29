from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
import userside.models
import userside.filters
import userside.forms
from django.urls import path, reverse


# Create your views here.


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'userside/index.html'
    # model = 'userside.courses'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return '!!!'


class courses(TitleMixin, ListView):
    title = 'Курсы'

    def get_filters(self):
        return userside.filters.CourseFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        # context['form'] = userside.forms.CourseCreate()
        context['filters'] = self.get_filters()
        return context


class course_detail(TitleMixin, DetailView):
    queryset = userside.models.course.objects.all()

    def get_title(self):
        return str(self.get_object())


class CourseUpdate(TitleMixin, UpdateView):
    model = userside.models.course
    form_class = userside.forms.Course

    def get_title(self):
        return f'Изменение данных курса "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseCreate(TitleMixin, CreateView):
    model = userside.models.course
    form_class = userside.forms.Course
    title = 'Добавление курса'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseDelete(TitleMixin, DeleteView):
    model = userside.models.course

    def get_title(self):
        return f'Удаление курса {str(self.get_object())}'

    def get_success_url(self):
        return reverse('userside:course_list')


# мои курсы


class mycourses(TitleMixin, ListView):

    title = 'Мои курсы'

    def get_filters(self):
        return userside.filters.MyCourseFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['filters'] = self.get_filters()
        return context


class mycourse_detail(TitleMixin, DetailView):

    queryset = userside.models.mycourse.objects.all()

    def get_title(self):
        obj_answer = self.get_object()
        time_course = obj_answer.name.length_of_time
        # print(f'стартовое время : {time_course} ч')
        delta_date = obj_answer.date_end - obj_answer.date_begin
        # print('количество дней изучения : ', delta_date.days)
        hour_study = delta_date.days*2
        # print('количество часов на изучение : ', hour_study)
        delta_hour = hour_study/time_course
        # print(delta_hour)
        # print(round(delta_hour))
        if round(delta_hour) == 1:
            answer = str(obj_answer) + '  :  ' + str(f' Изучение один раз в рабочий день, 2 ч.')
        else:
            answer = str(obj_answer) + '  :  ' + str(f'Изучение один раз в {round(delta_hour)} '
                                                 f'рабочих дней(я), 2 ч.')
        return answer


class MyCourseCreate(TitleMixin, CreateView):
    model = userside.models.mycourse
    form_class = userside.forms.MyCourseCreate
    title = 'Добавление курса'

    def get_success_url(self):
        return reverse('userside:mycourse_list')


class MyCourseUpdate(TitleMixin, UpdateView):
    model = userside.models.mycourse
    form_class = userside.forms.MyCourseEdit

    def get_title(self):
        return f'Изменение данных курса "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('userside:mycourse_list')


class MyCourseDelete(TitleMixin, DeleteView):
    model = userside.models.mycourse

    def get_title(self):
        return f'Удаление курса {str(self.get_object())}'

    def get_success_url(self):
        return reverse('userside:mycourse_list')


# преподаватели

class educators(TitleMixin, ListView):

    title = 'Преподаватели'

    def get_filters(self):
        return userside.filters.EducatorFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        # context['form'] = userside.forms.CourseCreate()
        context['filters'] = self.get_filters()
        return context


class educator_detail(TitleMixin, DetailView):

    queryset = userside.models.educator.objects.all()

    def get_title(self):
        return str(self.get_object())


class EducatorCreate(TitleMixin, CreateView):
    model = userside.models.educator
    form_class = userside.forms.Educator
    title = 'Добавление преподавателя'

    def get_success_url(self):
        return reverse('userside:educator_list')


class EducatorUpdate(TitleMixin, UpdateView):
    model = userside.models.educator
    form_class = userside.forms.Educator

    def get_title(self):
        return f'Изменение данных курса "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('userside:mycourse_list')


class EducatorDelete(TitleMixin, DeleteView):
    model = userside.models.educator

    def get_title(self):
        return f'Удаление преподавателя {str(self.get_object())}'

    def get_success_url(self):
        return reverse('userside:educator_list')


# уведомления

class Notice(TitleMixin, ListView):
    pass


# документы

class My_Documents(TitleMixin, ListView):
    pass