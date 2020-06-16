from django.urls import path

from . import views


urlpatterns = [
    path('courses/<slug:course_slug>/',
         views.CourseList, name='CourseListByCategory'),
    path('course/<slug:slug>/', views.CourseDetail, name='CourseDetail'),
    path('', views.CourseList, name='CourseList'),
]
