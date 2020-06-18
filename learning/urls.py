from django.urls import path

from learning import views

app_name = 'learning'

urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='course-list'),
    path('course/<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/<slug:course_slug>/lesson/', views.LessonListView.as_view(), name='lesson-list'),
    path('course/<slug:course_slug>/lesson/<slug:lesson_slug>/', views.LessonDetailView.as_view(), name='lesson-detail'),
]
