from django.test import TestCase
from ..serializers import TaskSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TaskSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username="user", password="pass")

    def test_valid_serializer(self):
        valid_data = {
            "title": "test task",
            "description": "test description",
            "is_completed": False,
        }
        serializer = TaskSerializer(data=valid_data, context={"request": self.user})
        self.assertTrue(serializer.is_valid())

    def test_missing_title(self):
        invalid_data = {
            "description": "missing title",
            "is_completed": False,
        }
        serializer = TaskSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)
