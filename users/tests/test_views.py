from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.tests.factories import UserFactory

User = get_user_model()


class ProfileViewTest(TestCase):
    def test_view_response_200(self):
        user = UserFactory()
        self.client.force_login(user)
        url = reverse('user:profile-detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ProfileUpdateViewTest(TestCase):
    def test_profile_can_be_updated(self):
        user = UserFactory()
        data = {
            'first_name': 'Вася',
            'last_name': 'Долгополов',
            'email': 'vasja@mail.ru',
        }
        self.client.force_login(user)
        url = reverse('user:profile-update')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, data.get('first_name'))
        self.assertEqual(user.last_name, data.get('last_name'))
        self.assertEqual(user.email, data.get('email'))


class LoginViewTest(TestCase):
    def test_user_can_login(self):
        u = UserFactory.build()
        u.set_password('123')
        u.active = True
        u.save()
        data = {
            'email': u.email,
            'password': '123',
        }
        url = reverse('account_login')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class SignupViewTest(TestCase):
    def test_user_can_be_created(self):
        data = {
            'first_name': 'Вася',
            'last_name': 'Долгополов',
            'email': 'vasja@mail.ru',
            'password1': 'Terminator672',
            'password2': 'Terminator672',
        }
        url = reverse('account_signup')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        u = User.objects.filter(email=data.get('email')).first()
        self.assertTrue(u)
        self.assertEqual(u.first_name, data.get('first_name'))
