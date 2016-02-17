"""
Test the accounts app
"""

from django.test import TestCase, Client

from model_mommy import mommy

from .models import User


class ViewsTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(email='email@email.com',
                                             password='password')

    def test_login_get_page(self):
        response = self.c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_post_creds(self):
        response = self.c.post('/accounts/login/', {'username': 'email@email.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.c.login(email='email@email.com', password='password')
        response = self.c.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)


class ModelsTests(TestCase):
    def test_user_unicode(self):
        user = mommy.make('accounts.User', email='test@test.com')
        self.assertEqual(unicode(user), 'test@test.com')

    def test_user_get_full_name(self):
        user = mommy.make('accounts.User', email='test@test.com')
        self.assertEqual(user.get_full_name(), 'test@test.com')
