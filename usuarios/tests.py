from django.test import TestCase
from .models import Users


class UsersTest(TestCase):
    def setUp(self):
        Users.objects.create(
            username='kenedy',
            email='kenedy@kenedy.com',
            password=123
        )

    def test_model_users(self):
        user = Users.objects.get(username='kenedy')
        self.assertEquals(user.__str__(), 'kenedy')
