from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
# from userside.forms import CourseSearch
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
    title = 'Begin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Go'


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
        # print(context)
        return context


class course_detail(TitleMixin, DetailView):
    queryset = userside.models.course.objects.all()

    def get_title(self):
        return str(self.get_object())


class CourseUpdate(TitleMixin, UpdateView):
    model = userside.models.course
    form_class = userside.forms.CourseEdit

    def get_title(self):
        return f'Изменение данных курса "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseCreate(TitleMixin, CreateView):
    model = userside.models.course
    form_class = userside.forms.CourseCreate
    title = 'Добавление курса'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseDelete(TitleMixin, DeleteView):
    model = userside.models.course

    def get_title(self):
        return f'Удаление курса {str(self.get_object())}'

    def get_success_url(self):
        return reverse('userside:course_list')
