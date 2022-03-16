from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.views.generic import TemplateView, ListView, DetailView

import userside.models
from django.urls import path
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


class mycourses(TitleMixin, ListView):
    title = 'курсы'

    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = userside.models.mycourse.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class course_detail(TitleMixin, DetailView):
    queryset = userside.models.mycourse.objects.all()

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
#     return render(request, 'userside/mycourse_list.html', {'courses': courses})

# def course_detail(request, pk):
#     course = get_object_or_404(userside.models.mycourse, pk=pk)
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!', course)
#     return render(request, 'userside/mycourse_detail.html', {'course': course})

