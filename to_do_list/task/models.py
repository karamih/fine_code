from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
