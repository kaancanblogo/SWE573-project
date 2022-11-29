from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your tests here.


class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='123test123', email='test@gmail.com')
        self.user.save()

    def test_correct(self):
        user = authenticate(username='testuser', password='123test123')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='not_testuser', password='123test123')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='testuser', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def tearDown(self):
        self.user.delete()
