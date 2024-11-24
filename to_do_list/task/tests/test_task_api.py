from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username="user", password="pass")
        self.client.login(username="user", password="pass")

        self.task_list_url = "/api/tasks/"

    def test_create_task(self):
        data = {"title": "task", "description": "description", "is_completed": False}
        response = self.client.post(self.task_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "task")

    def test_retrieve_tasks(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
