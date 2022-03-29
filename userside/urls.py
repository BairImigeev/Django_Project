from django.contrib import admin
from django.urls import path, include
import userside.views

app_name = 'userside'

urlpatterns = [
    path('', userside.views.IndexView.as_view(), name='index'),

    path('courses/', userside.views.courses.as_view(), name='course_list'),
    path('mycourses/', userside.views.mycourses.as_view(), name='mycourse_list'),
    path('educators/', userside.views.educators.as_view(), name='educator_list'),

    path('courses/<int:pk>/', userside.views.course_detail.as_view(), name='course_detail'),
    path('mycourses/<int:pk>/', userside.views.mycourse_detail.as_view(), name='mycourse_detail'),
    path('educators/<int:pk>/', userside.views.educator_detail.as_view(), name='educator_detail'),

    path('courses/create/', userside.views.CourseCreate.as_view(), name='course_create'),
    path('mycourses/create', userside.views.MyCourseCreate.as_view(), name='mycourse_create'),
    path('educators/create', userside.views.EducatorCreate.as_view(), name='educator_create'),


    path('courses/<int:pk>/update/', userside.views.CourseUpdate.as_view(), name='course_update'),
    path('mycourses/<int:pk>/update/', userside.views.MyCourseUpdate.as_view(), name='mycourse_update'),
    path('educators/<int:pk>/update/', userside.views.EducatorUpdate.as_view(), name='educator_update'),

    path('courses/<int:pk>/delete/', userside.views.CourseDelete.as_view(), name='course_delete'),
    path('mycourses/<int:pk>/delete/', userside.views.MyCourseDelete.as_view(), name='mycourse_delete'),
    path('educators/<int:pk>/delete/', userside.views.EducatorDelete.as_view(), name='educator_delete')

]
