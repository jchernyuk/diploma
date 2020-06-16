from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404

from .models import Course, Lessons


# class CourseView(ListView):
#     model = Course
#     queryset = Course.objects.all()
#     template_name = "courses/index.html"

# class CourseDetailView(DetailView):
#     model = Course
#     slug_field = "url"
#     template_name = "courses/course.html"


# отдаём в шаблон все курсы, потом если юзер выбирает курс активируется курс слаг и выдаёт уроки
# фильтруя по курсу

def CourseList(request, course_slug=None):
    course = None
    courses = Course.objects.all()
    lessons = Lessons.objects.all()

    if course_slug:
        course = get_object_or_404(Course, slug=course_slug)
        lessons = lessons.filter(course=course)
    return render(request, 'courses/list.html', {'course': course,
                                                 'courses': courses,
                                                 'lessons': lessons, })


def CourseDetail(request, slug):
    lesson = get_object_or_404(Lessons, slug=slug)
    return render(request, 'courses/detail.html', {'lesson': lesson, })


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.course = course
            form.save()
        return redirect(course.get_absolute_url())


# class LessonView(ListView):
#     model = Lessons
#     template_name = "courses/lesson_list.html"


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Course.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context[q] = self.request.GET.get("q")
        return context
