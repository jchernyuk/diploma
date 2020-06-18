from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site

from learning.models import CourseAreas, TypeRating, FormatCourse, \
    Language, Course, CourseShots, Reviews, Lesson, Poll, PollAnswer

admin.site.register(CourseAreas)
admin.site.register(TypeRating)
admin.site.register(FormatCourse)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(CourseShots)
admin.site.register(Reviews)
admin.site.register(Lesson)
admin.site.register(Poll)
admin.site.register(PollAnswer)
admin.site.unregister(Site)
admin.site.unregister(Group)
