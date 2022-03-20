from django.contrib import admin
from django.urls import path, include
import userside.views

app_name = 'userside'

urlpatterns = [
    path('', userside.views.IndexView.as_view(), name='index'),
    path('courses/', userside.views.course.as_view(), name='course_list'),
    path('courses/<int:pk>/', userside.views.course_detail.as_view(), name='course_detail'),
    path('courses/create/', userside.views.CourseCreate.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', userside.views.CourseUpdate.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', userside.views.CourseDelete.as_view(), name='course_delete'),
]
