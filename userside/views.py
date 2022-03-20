from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from userside.forms import CourseSearch
import userside.models
import userside.filters
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


class course(TitleMixin, ListView):
    title = 'Курсы'

    def get_filters(self):
        return userside.filters.CourseFilter(self.request.GET)

    def get_queryset(self):
        # name = self.request.GET.get('name')
        # queryset = userside.models.mycourse.objects.all()
        # if name:
        #     queryset = queryset.filter(name__icontains=name)
        # return queryset
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        # context['form'] = CourseSearch(self.request.GET or None)
        context['filters'] = self.get_filters()
        print(context)
        return context


class course_detail(TitleMixin, DetailView):

    queryset = userside.models.course.objects.all()

    def get_title(self):
        return str(self.get_object())
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['title'] = str(self.get_object())
    #     return context


# def index(request):
#     courses = userside.models.mycourse.objects.all()
#     return render(request, 'userside/index.html', {'courses': courses})


# def mycourses(request):
#     name = request.GET.get('name')
#     courses = userside.models.mycourse.objects.all()
#     if name:
#         courses = courses.filter(name__icontains=name)
#     return render(request, 'userside/course_list.html', {'courses': courses})

# def course_detail(request, pk):
#     course = get_object_or_404(userside.models.mycourse, pk=pk)
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!', course)
#     return render(request, 'userside/course_detail.html', {'course': course})

class CourseUpdate(TitleMixin, UpdateView):
    model = userside.models.course
    form_class = userside.forms.CourseEdit

    def get_title(self):
        return f'Изменение данных курса "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseCreate(TitleMixin, CreateView):
    model = userside.models.course
    form_class = userside.forms.CourseEdit
    title = 'Добавление курса'

    def get_success_url(self):
        return reverse('userside:course_list')


class CourseDelete(TitleMixin, DeleteView):
    model = userside.models.course

    def get_title(self):
        return f'Удаление курса {str(self.get_object())}'

    def get_success_url(self):
        return reverse('userside:course_list')
