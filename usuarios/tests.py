from django.test import TestCase
from .models import Users
from .serializers import UsersSerializer
from django.urls import reverse


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

    def test_serializers_users(self):
        serializer_user = UsersSerializer(data={
            'username': 'kenedy',
            'email': 'kenedy@kenedy',
            'password': 123
        })
        self.assertTrue(serializer_user.is_valid())
