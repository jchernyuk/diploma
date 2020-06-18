from django.test import TestCase
from django.urls import reverse

from learning.tests.factories import CourseFactory, LessonFactory


class IndexViewTest(TestCase):
    def test_view_response_200(self):
        url = reverse('learning:course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CoursesListViewTest(TestCase):
    def test_view_response_200(self):
        url = reverse('learning:course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CourseDetailViewTest(TestCase):
    def test_view_response_200(self):
        course = CourseFactory()
        response = self.client.get(course.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_review_can_be_posted(self):
        course = CourseFactory()
        data = {
            'name': 'Igor Serdukov',
            'email': 'serdukov@mail.ru',
            'text': 'Привет, лунатикам!',
        }
        response = self.client.post(course.get_absolute_url(), data)
        course.refresh_from_db()
        self.assertTrue(course.reviews.exists())


class LessonDetailViewTest(TestCase):
    def test_view_response_200(self):
        lesson = LessonFactory()
        response = self.client.get(lesson.get_absolute_url())
        self.assertEqual(response.status_code, 200)
