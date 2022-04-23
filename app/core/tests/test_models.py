from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_model_with_email(self):
        """Test create new user model"""
        email = "arul@kandhan.com"
        password = "Pass@123"

        user = get_user_model().objects.create_user(
              email = email,
              password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Normalise the email address"""
        email = "arul@KANDAN.com"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())


    def test_email_address(self):
        """Test the email address is mandatory with raise"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test the super is created successfully"""
        user = get_user_model().objects.create_super_user(
             email = 'arul@gmail.com',
             password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
