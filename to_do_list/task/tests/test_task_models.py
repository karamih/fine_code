from django.test import TestCase
from ..models import Task
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username="user", password="pass")
        self.task = Task.objects.create(
            user=self.user, title="test task", description="test description", is_completed=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "test task")
        self.assertEqual(self.task.user, self.user)
        self.assertFalse(self.task.is_completed)

    def test_str_representation(self):
        self.assertEqual(str(self.task), "test task")
