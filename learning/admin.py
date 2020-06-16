from django.contrib import admin

from .models import CourseAreas, TypeRating, FormatCourse, Language, Course, CourseShots, Reviews, Lessons
admin.site.register(CourseAreas)
admin.site.register(TypeRating)
admin.site.register(FormatCourse)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(CourseShots)
admin.site.register(Reviews)
admin.site.register(Lessons)


# class TestQuestionsInline(admin.TabularInline):
#     model = TestQuestion
#
# @admin.register(Lessons)
# class LessonsAdmin(admin.ModelAdmin):
#     inlines = [TestQuestionsInline]