from django.contrib import admin
from django.urls import path, include
import userside.views

app_name = 'userside'

urlpatterns = [
    path('', userside.views.IndexView.as_view(), name='index'),
    path('mycourses/', userside.views.mycourses.as_view(), name='mycourses'),
    path('mycourses/<int:pk>/', userside.views.course_detail.as_view(), name='course_detail')
]
