from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import ReviewForm
from .models import Course, Lesson


class IndexView(ListView):
    model = Course
    template_name = 'learning/index.html'


class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        return qs


class CourseDetailView(FormMixin, DetailView):
    model = Course
    form_class = ReviewForm

    def get_success_url(self):
        return self.get_object().get_absolute_url()

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.course = self.get_object()
        review.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        obj = self.get_object()
        data.update({
            'reviews': obj.reviews.all()
        })
        return data


class LessonListView(ListView):
    model = Lesson

    def get_queryset(self):
        obj = get_object_or_404(
            Course,
            slug=self.kwargs.get('course_slug'),
        )
        return obj.lessons.all()


class LessonDetailView(DetailView):
    model = Lesson

    def get_object(self, queryset=None):
        return get_object_or_404(
            Lesson,
            course__slug=self.kwargs.get('course_slug'),
            slug=self.kwargs.get('lesson_slug'),

        )
