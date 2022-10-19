from django.test import TestCase
from django.contrib.auth import get_user_model


class ProfileTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='12test12',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_read_profile(self):
        self.assertEqual(str(self.user.profile), 'test Profile')
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue('default.jpg' in self.user.profile.image.url)

    def test_update_username(self):
        self.user.username = 'test777'
        self.user.save()
        self.assertEqual(self.user.username, 'test777')

    def test_update_email(self):
        self.user.email = 'test777@example.com'
        self.user.save()
        self.assertEqual(self.user.email, 'test777@example.com')
